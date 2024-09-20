"""`pygerber.nodes.aperture.ADP` module contains definition of `AD` class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Optional

from pydantic import Field

from pygerber.gerberx3.ast.nodes.aperture.AD import AD
from pygerber.gerberx3.ast.nodes.types import Double

if TYPE_CHECKING:
    from typing_extensions import Self

    from pygerber.gerberx3.ast.ast_visitor import AstVisitor


class ADR(AD):
    """Represents AD rectangle Gerber extended command."""

    width: Double
    height: Double
    hole_diameter: Optional[Double] = Field(default=None)

    def visit(self, visitor: AstVisitor) -> ADR:
        """Handle visitor call."""
        return visitor.on_adr(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], ADR]:
        """Get callback function for the node."""
        return visitor.on_adr