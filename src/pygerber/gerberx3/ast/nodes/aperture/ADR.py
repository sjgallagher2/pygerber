"""`pygerber.nodes.aperture.ADP` module contains definition of `AD` class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pydantic import Field

from pygerber.gerberx3.ast.nodes.base import Node

if TYPE_CHECKING:
    from pygerber.gerberx3.ast.visitor import AstVisitor


class ADR(Node):
    """Represents AD rectangle Gerber extended command."""

    aperture_identifier: str
    width: str
    height: str
    hole_diameter: Optional[str] = Field(default=None)

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_adr(self)
