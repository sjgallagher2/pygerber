"""`shape` module contains classes for drawing shapes consisting of connected lines
and arcs filled with solid color.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, List

import pyparsing as pp
from pydantic import BaseModel, Field

from pygerber.vm.commands.command import Command
from pygerber.vm.types.box import AutoBox
from pygerber.vm.types.vector import Vector

if TYPE_CHECKING:
    from typing_extensions import Self

    from pygerber.vm.base import CommandVisitor


class ShapeSegment(BaseModel):
    """Base class for shape segment types."""

    @pp.cached_property
    def outer_box(self) -> AutoBox:
        """Get outer box of shape segment."""
        raise NotImplementedError


class Line(ShapeSegment):
    """Draw a line from the current position to the given position."""

    start: Vector
    end: Vector

    @classmethod
    def from_tuples(cls, start: tuple[float, float], end: tuple[float, float]) -> Self:
        """Create a new line from two tuples."""
        return cls(start=Vector.from_tuple(start), end=Vector.from_tuple(end))

    @pp.cached_property
    def outer_box(self) -> AutoBox:
        """Get outer box of shape segment."""
        return AutoBox.from_vectors(self.start, self.end)


class Arc(ShapeSegment):
    """Draw a arc from the current position to the given position.

    Arcs are always clockwise.
    """

    start: Vector
    end: Vector
    center: Vector
    clockwise: bool

    @classmethod
    def from_tuples(
        cls,
        start: tuple[float, float],
        end: tuple[float, float],
        center: tuple[float, float],
        *,
        clockwise: bool,
    ) -> Self:
        """Create a new arc from two tuples."""
        return cls(
            start=Vector.from_tuple(start),
            end=Vector.from_tuple(end),
            center=Vector.from_tuple(center),
            clockwise=clockwise,
        )

    def get_relative_start_point(self) -> Vector:
        """Get starting point relative to arc center."""
        return self.start - self.center

    def get_relative_end_point(self) -> Vector:
        """Get ending point relative to arc center."""
        return self.end - self.center

    def get_radius(self) -> float:
        """Get radius of circle arc."""
        return self.get_relative_start_point().length()

    @pp.cached_property
    def outer_box(self) -> AutoBox:
        """Get outer box of shape segment."""
        radius = self.get_radius()
        relative_start = self.get_relative_start_point()

        total_angle = relative_start.angle_between(
            self.get_relative_end_point(),
        )

        angle_x_plus = relative_start.angle_between(Vector.unit.x) % 360
        angle_y_minus = relative_start.angle_between(-Vector.unit.y) % 360
        angle_x_minus = relative_start.angle_between(-Vector.unit.x) % 360
        angle_y_plus = relative_start.angle_between(Vector.unit.y) % 360

        vectors = [
            Vector(x=0, y=0),
            relative_start,
            self.get_relative_end_point(),
        ]
        if not self.clockwise:
            total_angle = 360 - total_angle
            angle_x_plus = 360 - angle_x_plus
            angle_y_minus = 360 - angle_y_minus
            angle_x_minus = 360 - angle_x_minus
            angle_y_plus = 360 - angle_y_plus

        if angle_x_plus < total_angle:
            vectors.append(Vector(x=radius, y=0))
        if angle_y_minus < total_angle:
            vectors.append(Vector(x=0, y=-radius))
        if angle_x_minus < total_angle:
            vectors.append(Vector(x=-radius, y=0))
        if angle_y_plus < total_angle:
            vectors.append(Vector(x=0, y=radius))

        return AutoBox.from_vectors(*(v + self.center for v in vectors))


class Shape(Command):
    """`Shape` command instructs VM to render a shape described by series of
    lines and arcs into currently active layer.

    Last point of first segment (line or arc) is always connected to the first point
    first segment, so shapes are implicitly closed. If those points are not overlapping,
    they are connected by a straight line.
    """

    commands: List[ShapeSegment] = Field(min_length=1)
    negative: bool = False

    @pp.cached_property
    def outer_box(self) -> AutoBox:
        """Get outer box of shape segment."""
        accumulator = self.commands[0].outer_box
        for segment in self.commands[1:]:
            accumulator += segment.outer_box
        return accumulator

    def visit(self, visitor: CommandVisitor) -> None:
        """Visit polygon command."""
        visitor.on_shape(self)

    @classmethod
    def new_rectangle(
        cls, center: tuple[float, float], width: float, height: float, *, negative: bool
    ) -> Self:
        """Create polygon in shape of rectangle."""
        half_height = height / 2
        half_width = width / 2
        return cls(
            commands=[
                Line.from_tuples(
                    (center[0] - half_width, center[1] - half_height),
                    (center[0] + half_width, center[1] - half_height),
                ),
                Line.from_tuples(
                    (center[0] + half_width, center[1] - half_height),
                    (center[0] + half_width, center[1] + half_height),
                ),
                Line.from_tuples(
                    (center[0] + half_width, center[1] + half_height),
                    (center[0] - half_width, center[1] + half_height),
                ),
                Line.from_tuples(
                    (center[0] - half_width, center[1] + half_height),
                    (center[0] - half_width, center[1] - half_height),
                ),
            ],
            negative=negative,
        )

    @classmethod
    def new_circle(
        cls, center: tuple[float, float], diameter: float, *, negative: bool
    ) -> Self:
        """Create polygon in shape of circle."""
        radius = diameter / 2
        return cls(
            commands=[
                Arc.from_tuples(
                    (center[0] - radius, center[1]),
                    (center[0] + radius, center[1]),
                    center=center,
                    clockwise=True,
                ),
                Arc.from_tuples(
                    (center[0] + radius, center[1]),
                    (center[0] - radius, center[1]),
                    center=center,
                    clockwise=True,
                ),
            ],
            negative=negative,
        )

    @classmethod
    def new_cw_arc(
        cls,
        start: tuple[float, float],
        end: tuple[float, float],
        center: tuple[float, float],
        thickness: float,
        *,
        negative: bool,
    ) -> Self:
        """Create polygon in shape of circle."""
        start_vector = Vector.from_tuple(start)
        extend_start_vector = start_vector.normalized() * (thickness / 2)

        end_vector = Vector.from_tuple(end)
        extend_end_vector = end_vector.normalized() * (thickness / 2)

        center_vector = Vector.from_tuple(center)

        return cls(
            commands=[
                Arc(
                    start=start_vector + extend_start_vector,
                    end=end_vector + extend_end_vector,
                    center=center_vector,
                    clockwise=True,
                ),
                Arc(
                    start=end_vector - extend_end_vector,
                    end=start_vector - extend_start_vector,
                    center=center_vector,
                    clockwise=False,
                ),
            ],
            negative=negative,
        )
