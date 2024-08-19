"""`pygerber.nodes.properties.FS` module contains definition of `FS` class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from pygerber.gerberx3.ast.nodes.base import Node
from pygerber.gerberx3.ast.nodes.enums import CoordinateMode, Zeros

if TYPE_CHECKING:
    from typing_extensions import Self

    from pygerber.gerberx3.ast.visitor import AstVisitor


class FS(Node):
    """Represents FS Gerber extended command."""

    zeros: Zeros
    coordinate_mode: CoordinateMode

    x_integral: int
    x_decimal: int

    y_integral: int
    y_decimal: int

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_fs(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_fs
