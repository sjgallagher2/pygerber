"""`pygerber.nodes.d_codes.TO` module contains definition of `TO` class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable, List, Optional

from pydantic import Field

from pygerber.gerberx3.ast.nodes.base import Node
from pygerber.gerberx3.ast.nodes.enums import Mount
from pygerber.gerberx3.ast.nodes.types import Double

if TYPE_CHECKING:
    from typing_extensions import Self

    from pygerber.gerberx3.ast.visitor import AstVisitor


class TO(Node):
    """Represents TO Gerber extended command."""

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        raise NotImplementedError


class TO_UserName(TO):  # noqa: N801
    """Represents TO Gerber extended command with user name."""

    user_name: str
    fields: List[str] = Field(default_factory=list)

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return self.user_name

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_user_name(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_user_name


class TO_N(TO):  # noqa: N801
    """Represents TO Gerber extended command with .N attribute."""

    net_names: List[str] = Field(default_factory=list)

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".N"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_n(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_n


class TO_P(TO):  # noqa: N801
    """Represents TO Gerber extended command with .P attribute."""

    refdes: str
    number: str
    function: Optional[str] = Field(default=None)

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".P"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_p(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_p


class TO_C(TO):  # noqa: N801
    """Represents TO Gerber extended command with .C attribute."""

    refdes: str

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".C"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_c(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_c


class TO_CRot(TO):  # noqa: N801
    """Represents TO Gerber extended command with .CRot attribute."""

    angle: Double

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".CRot"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_crot(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_crot


class TO_CMfr(TO):  # noqa: N801
    """Represents TO Gerber extended command with .CMfr attribute."""

    manufacturer: str

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".CMfr"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_cmfr(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_cmfr


class TO_CMNP(TO):  # noqa: N801
    """Represents TO Gerber extended command with .CMNP attribute."""

    part_number: str

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".CMNP"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_cmnp(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_cmnp


class TO_CVal(TO):  # noqa: N801
    """Represents TO Gerber extended command with .CVal attribute."""

    value: str

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".CVal"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_cval(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_cval


class TO_CMnt(TO):  # noqa: N801
    """Represents TO Gerber extended command with .CMnt attribute."""

    mount: Mount

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".CMnt"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_cmnt(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_cmnt


class TO_CFtp(TO):  # noqa: N801
    """Represents TO Gerber extended command with .CFtp attribute."""

    footprint: str

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".CFtp"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_cftp(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_cftp


class TO_CPgN(TO):  # noqa: N801
    """Represents TO Gerber extended command with .CPgN attribute."""

    name: str

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".CPgN"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_cpgn(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_cpgn


class TO_CPgD(TO):  # noqa: N801
    """Represents TO Gerber extended command with .CPgD attribute."""

    description: str

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".CPgD"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_cpgd(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_cpgd


class TO_CHgt(TO):  # noqa: N801
    """Represents TO Gerber extended command with .CHgt attribute."""

    height: Double

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".CHgt"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_chgt(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_chgt


class TO_CLbN(TO):  # noqa: N801
    """Represents TO Gerber extended command with .CLbN attribute."""

    name: str

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".CLbN"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_clbn(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_clbn


class TO_CLbD(TO):  # noqa: N801
    """Represents TO Gerber extended command with .CLbD attribute."""

    description: str

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".CLbD"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_clbd(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_clbd


class TO_CSup(TO):  # noqa: N801
    """Represents TO Gerber extended command with .CSup attribute."""

    supplier: str
    supplier_part: str

    other_suppliers: List[str] = Field(default_factory=list)

    @property
    def attribute_name(self) -> str:
        """Get attribute name."""
        return ".CSup"

    def visit(self, visitor: AstVisitor) -> None:
        """Handle visitor call."""
        visitor.on_to_csup(self)

    def get_visitor_callback_function(
        self, visitor: AstVisitor
    ) -> Callable[[Self], None]:
        """Get callback function for the node."""
        return visitor.on_to_csup
