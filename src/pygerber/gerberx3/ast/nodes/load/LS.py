"""`pygerber.nodes.load.LS` module contains definition of `LS` class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from pygerber.gerberx3.ast.nodes.base import Node
from pygerber.gerberx3.ast.nodes.types import Double

if TYPE_CHECKING:
    from typing_extensions import Self

    from pygerber.gerberx3.ast.visitor import AstVisitor


class LS(Node):
    """Represents LS Gerber extended command."""

    scale: Double

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_ls(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_ls
