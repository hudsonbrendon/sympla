import pytest

from sympla import Sympla


@pytest.fixture
def sympla():
    return Sympla("test")
