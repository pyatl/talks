from fifteen_puzzle import Puzzle

import pytest


@pytest.fixture
def puzzle():
    """Fixture providing a new Puzzle of the default size (4x4)"""

    return Puzzle()
