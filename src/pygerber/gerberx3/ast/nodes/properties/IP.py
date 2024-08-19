"""`pygerber.nodes.properties.IP` module contains definition of `IP` class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from pygerber.gerberx3.ast.nodes.base import Node
from pygerber.gerberx3.ast.nodes.enums import ImagePolarity

if TYPE_CHECKING:
    from typing_extensions import Self

    from pygerber.gerberx3.ast.visitor import AstVisitor


class IP(Node):
    """Represents IP Gerber extended command."""

    polarity: ImagePolarity

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_ip(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_ip
