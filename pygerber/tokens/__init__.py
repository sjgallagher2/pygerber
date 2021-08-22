# -*- coding: utf-8 -*-
from typing import List, Type

from pygerber.tokens.token import Token

from .add import ADD_Token
from .comment import G04Token, G74Token, G75Token
from .dnn import D01_Token, D02_Token, D03_Token, DNN_Loader_Token
from .fs import FormatSpecifierToken
from .gnn import G0N_Token, G36_Token, G37_Token
from .load import (
    LoadPolarityToken,
    LoadMirroringToken,
    LoadRotationToken,
    LoadScalingToken,
    LoadUnitToken,
)
from .control import EndOfStream_Token, Whitespace_Token
from .am import ApertureMacro_Token

token_classes: List[Type[Token]] = [
    Whitespace_Token,
    FormatSpecifierToken,
    D01_Token,
    D02_Token,
    D03_Token,
    DNN_Loader_Token,
    ADD_Token,
    G04Token,
    G74Token,
    G75Token,
    G0N_Token,
    G36_Token,
    G37_Token,
    LoadPolarityToken,
    LoadMirroringToken,
    LoadRotationToken,
    LoadScalingToken,
    LoadUnitToken,
    EndOfStream_Token,
    ApertureMacro_Token,
]
