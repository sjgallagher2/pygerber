"""`pygerber.nodes.math.point` module contains definition of `Point`
class.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from pygerber.gerberx3.ast.nodes.base import Node
from pygerber.gerberx3.ast.nodes.math.expression import Expression

if TYPE_CHECKING:
    from typing_extensions import Self

    from pygerber.gerberx3.ast.ast_visitor import AstVisitor


class Point(Node):
    """Represents math point point."""

    x: Expression
    y: Expression

    def visit(self, visitor: AstVisitor) -> Point:
        """Handle visitor call."""
        return visitor.on_point(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], Point]:
        """Get callback function for the node."""
        return visitor.on_point