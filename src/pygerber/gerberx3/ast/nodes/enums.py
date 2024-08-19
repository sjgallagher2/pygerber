"""`pygerber.gerberx3.ast.nodes.enums` module contains definition of enums used in
GerberX3 AST nodes.
"""

from __future__ import annotations

from enum import Enum


class Zeros(Enum):
    """Zeros enumeration."""

    SKIP_LEADING = "L"
    """Skip leading zeros mode."""

    SKIP_TRAILING = "T"
    """Skip trailing zeros mode."""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"

    __str__ = __repr__


class CoordinateMode(Enum):
    """Coordinate mode enumeration."""

    ABSOLUTE = "A"
    """Absolute coordinate mode."""

    INCREMENTAL = "I"
    """Incremental coordinate mode."""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"

    __str__ = __repr__


class AperFunction(Enum):
    """Enum representing possible AperFunction values."""

    ViaDrill = "ViaDrill"
    BackDrill = "BackDrill"
    ComponentDrill = "ComponentDrill"
    MechanicalDrill = "MechanicalDrill"
    CastellatedDrill = "CastellatedDrill"
    OtherDrill = "OtherDrill"
    ComponentPad = "ComponentPad"
    SMDPad = "SMDPad"
    BGAPad = "BGAPad"
    ConnectorPad = "ConnectorPad"
    HeatsinkPad = "HeatsinkPad"
    ViaPad = "ViaPad"
    TestPad = "TestPad"
    CastellatedPad = "CastellatedPad"
    FiducialPad = "FiducialPad"
    ThermalReliefPad = "ThermalReliefPad"
    WasherPad = "WasherPad"
    AntiPad = "AntiPad"
    OtherPad = "OtherPad"
    Conductor = "Conductor"
    EtchedComponent = "EtchedComponent"
    NonConductor = "NonConductor"
    CopperBalancing = "CopperBalancing"
    Border = "Border"
    OtherCopper = "OtherCopper"
    ComponentMain = "ComponentMain"
    ComponentOutline = "ComponentOutline"
    ComponentPin = "ComponentPin"
    Profile = "Profile"
    Material = "Material"
    NonMaterial = "NonMaterial"
    Other = "Other"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"

    __str__ = __repr__


class Part(Enum):
    """Enumerate supported part types."""

    Single = "Single"
    Array = "Array"
    FabricationPanel = "FabricationPanel"
    Coupon = "Coupon"
    Other = "Other"


class FileFunction(Enum):
    """Enumerate supported file function types."""

    Copper = "Copper"
    Plated = "Plated"
    NonPlated = "NonPlated"
    Profile = "Profile"
    Soldermask = "Soldermask"
    Legend = "Legend"
    Component = "Component"
    Paste = "Paste"
    Glue = "Glue"
    Carbonmask = "Carbonmask"
    Goldmask = "Goldmask"
    Heatsinkmask = "Heatsinkmask"
    Peelablemask = "Peelablemask"
    Silvermask = "Silvermask"
    Tinmask = "Tinmask"
    Depthrout = "Depthrout"
    Vcut = "Vcut"
    Viafill = "Viafill"
    Pads = "Pads"
    Other = "Other"
    Drillmap = "Drillmap"
    FabricationDrawing = "FabricationDrawing"
    Vcutmap = "Vcutmap"
    AssemblyDrawing = "AssemblyDrawing"
    ArrayDrawing = "ArrayDrawing"
    OtherDrawing = "OtherDrawing"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"

    __str__ = __repr__


class Mount(Enum):
    """Mount type enumeration."""

    SMD = "SMD"
    TH = "TH"
    Pressfit = "Pressfit"
    Fiducial = "Fiducial"
    Other = "Other"


class Mirroring(Enum):
    """Mirroring enum."""

    None_ = "N"
    X = "X"
    Y = "Y"
    XY = "XY"


class Polarity(Enum):
    """Polarity enum."""

    Clear = "C"
    Dark = "D"


class AxisCorrespondence(Enum):
    """Represents axis correspondence."""

    AX_BY = "AXBY"
    AY_BX = "AYBX"


class UnitMode(Enum):
    """Unit mode enumeration."""

    IMPERIAL = "IN"
    """Imperial unit mode. In this mode inches are used to express lengths."""
    METRIC = "MM"
    """Metric unit mode. In this mode millimeters are used to express lengths."""


class ImagePolarity(Enum):
    """Image polarity enumeration."""

    POSITIVE = "POS"
    """Positive image polarity."""

    NEGATIVE = "NEG"
    """Negative image polarity."""
