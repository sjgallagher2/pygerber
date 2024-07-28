"""`pygerber.nodes.d_codes.D01` module contains definition of `D01` class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pydantic import Field

from pygerber.gerberx3.ast.nodes.base import Node
from pygerber.gerberx3.ast.nodes.other.coordinate import (
    CoordinateI,
    CoordinateJ,
    CoordinateX,
    CoordinateY,
)

if TYPE_CHECKING:
    from pygerber.gerberx3.ast.visitor import AstVisitor


class D01(Node):
    """Represents D01 Gerber command."""

    x: Optional[CoordinateX] = Field(default=None)
    y: Optional[CoordinateY] = Field(default=None)
    i: Optional[CoordinateI] = Field(default=None)
    j: Optional[CoordinateJ] = Field(default=None)

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_d01(self)
