"""`pygerber.nodes.g_codes.G01` module contains definition of `G01` class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from pygerber.gerberx3.ast.nodes.g_codes.G import G

if TYPE_CHECKING:
    from typing_extensions import Self

    from pygerber.gerberx3.ast.ast_visitor import AstVisitor


class G01(G):
    """Represents G01 Gerber command."""

    def visit(self, visitor: AstVisitor) -> G01:
        """Handle visitor call."""
        return visitor.on_g01(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], G01]:
        """Get callback function for the node."""
        return visitor.on_g01
