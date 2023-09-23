"""Wrapper for G70 token."""
from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Iterable, Tuple

from pygerber.gerberx3.state_enums import Unit
from pygerber.gerberx3.tokenizer.tokens.token import Token
from pygerber.warnings import warn_deprecated_code

if TYPE_CHECKING:
    from pygerber.backend.abstract.backend_cls import Backend
    from pygerber.backend.abstract.draw_commands.draw_command import DrawCommand
    from pygerber.gerberx3.parser.state import State


class SetUnitInch(Token):
    """Wrapper for G70 token.

    Set the `Unit` to inch.

    This historic codes perform a function handled by the MO command. See 4.2.1.
    Sometimes used. Deprecated in 2012

    See section 8.1 of The Gerber Layer Format Specification Revision 2023.03 - https://argmaster.github.io/pygerber/latest/gerber_specification/revision_2023_03.html
    """

    def update_drawing_state(
        self,
        state: State,
        _backend: Backend,
    ) -> Tuple[State, Iterable[DrawCommand]]:
        """Set drawing polarity."""
        warn_deprecated_code("G70", "8.1")
        logging.warning(
            "Detected use of imperial units. Using metric units is recommended. "
            "Imperial units will be deprecated in future. "
            "(See 4.2.1 in Gerber Layer Format Specification)",
        )
        if state.draw_units is not None:
            logging.warning(
                "Overriding coordinate units is illegal. "
                "(See section 4.2.2 of The Gerber Layer Format Specification "
                "Revision 2023.03 - https://argmaster.github.io/pygerber/latest/gerber_specification/revision_2023_03.html)",
            )
        return (
            state.model_copy(
                update={
                    "draw_units": Unit.Inches,
                },
            ),
            (),
        )

    def get_gerber_code(
        self,
        indent: str = "",
        endline: str = "\n",  # noqa: ARG002
    ) -> str:
        """Get gerber code represented by this token."""
        return f"{indent}G70*"
