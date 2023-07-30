"""Tokenizer tests based on basic examples."""
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pathlib import Path

from test.gerberx3.common import (
    find_gerberx3_asset_files,
    save_token_stack,
    tokenize_gerberx3,
)

if TYPE_CHECKING:
    from test.conftest import AssetLoader


@pytest.mark.parametrize(
    ["directory", "file_name"],
    sorted(find_gerberx3_asset_files("test/assets/gerberx3/basic")),
)
def test_sample(asset_loader: AssetLoader, directory: Path, file_name: str) -> None:
    """Test tokenizer on sample gerber code."""
    stack = tokenize_gerberx3(asset_loader, directory, file_name)
    save_token_stack(stack, __file__, directory, file_name)