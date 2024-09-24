"""`compiler` module contains internals of Gerber X3 to RVMC compiler."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pygerber.gerberx3.ast.nodes import File
from pygerber.gerberx3.compiler.compiler import Compiler
from pygerber.gerberx3.compiler.errors import CompilerError, CyclicBufferDependencyError

if TYPE_CHECKING:
    from pygerber.vm.rvmc import RVMC

__all__ = ["Compiler", "CompilerError", "CyclicBufferDependencyError"]


def compile(ast: File, *, ignore_program_stop: bool = False) -> RVMC:  # noqa: A001
    """Compile GerberX3 AST to RVMC code.

    Parameters
    ----------
    ast : File
        Gerber abstract syntax tree.
    ignore_program_stop : bool, optional
        Toggle ignoring M00/M02 instructions, by default False

    Returns
    -------
    RVMC
        Generated virtual machine instructions.

    """
    return Compiler(ignore_program_stop=ignore_program_stop).compile(ast)
