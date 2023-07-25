"""Tokenizer tests based on A64-OLinuXino-rev-G project."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from pygerber.gerberx3.tokenizer.tokenizer import Tokenizer

from pygerber.gerberx3.parser.parser import Parser

if TYPE_CHECKING:
    from test.conftest import AssetLoader


def test_A64_OlinuXino_Rev_G_B_Mask(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-B_Mask file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-B_Mask.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()


def test_A64_OlinuXino_Rev_G_In3_Cu(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-In3_Cu file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-In3_Cu.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()


def test_A64_OlinuXino_Rev_G_In1_Cu(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-In1_Cu file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-In1_Cu.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()


def test_A64_OlinuXino_Rev_G_In4_Cu(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-In4_Cu file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-In4_Cu.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()


def test_A64_OlinuXino_Rev_G_F_Paste(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-F_Paste file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-F_Paste.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()


def test_A64_OlinuXino_Rev_G_B_Paste(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-B_Paste file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-B_Paste.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()


def test_A64_OlinuXino_Rev_G_B_Cu(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-B_Cu file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-B_Cu.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()


def test_A64_OlinuXino_Rev_G_Edge_Cuts(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-Edge_Cuts file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-Edge_Cuts.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()


def test_A64_OlinuXino_Rev_G_F_Cu(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-F_Cu file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-F_Cu.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()


@pytest.mark.xfail(reason="No support for G0X merged with D01")
def test_A64_OlinuXino_Rev_G_F_SilkS(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-F_SilkS file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-F_SilkS.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()


@pytest.mark.xfail(reason="No support for G0X merged with D01")
def test_A64_OlinuXino_Rev_G_B_SilkS(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-B_SilkS file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-B_SilkS.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()


def test_A64_OlinuXino_Rev_G_In2_Cu(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-In2_Cu file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-In2_Cu.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()


def test_A64_OlinuXino_Rev_G_F_Mask(
    asset_loader: AssetLoader,
) -> None:
    """Parser test based on A64-OlinuXino_Rev_G-F_Mask file."""
    stack = Tokenizer().tokenize(
        asset_loader.load_asset(
            "gerberx3/A64-OLinuXino-rev-G/A64-OlinuXino_Rev_G-F_Mask.gbr"
        ).decode("utf-8"),
    )

    parser = Parser(stack)
    parser.parse()
