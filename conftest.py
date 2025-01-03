import pytest

from sympla import Sympla


@pytest.fixture
def sympla() -> Sympla:
    return Sympla("test")
