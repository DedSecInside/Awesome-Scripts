import pathlib

import pytest


@pytest.fixture
def docs_dir():
    """
    Return the path to the given dir.

    Args:
    """
    return pathlib.Path('readthedocs')
