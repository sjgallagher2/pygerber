"""`pygerber.nodes.math.assignment` module contains definition of `Assignment` class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pygerber.gerberx3.ast.nodes.base import Node
from pygerber.gerberx3.ast.nodes.math.expression import Expression
from pygerber.gerberx3.ast.nodes.math.variable import Variable

if TYPE_CHECKING:
    from pygerber.gerberx3.ast.visitor import AstVisitor


class Assignment(Node):
    """Represents math expression variable."""

    variable: Variable
    expression: Expression

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_assignment(self)
