"""`pygerber.nodes.math.variable` module contains definition of `Variable` class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from pygerber.gerberx3.ast.nodes.math.expression import Expression

if TYPE_CHECKING:
    from typing_extensions import Self

    from pygerber.gerberx3.ast.visitor import AstVisitor


class Variable(Expression):
    """Represents math expression variable."""

    variable: str

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_variable(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_variable
