"""Outline macro primitive."""
from __future__ import annotations

from typing import List

from pygerber.gerberx3.parser2.macro2.expressions2.expression2 import Expression2
from pygerber.gerberx3.parser2.macro2.point2 import Point2
from pygerber.gerberx3.parser2.macro2.primitives2.primitive2 import Primitive2


class Code4Outline2(Primitive2):
    """Vector line macro primitive."""

    exposure: Expression2
    vertex_count: Expression2
    start_x: Expression2
    start_y: Expression2
    points: List[Point2]
    rotation: Expression2
