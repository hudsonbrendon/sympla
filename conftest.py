import pytest

from pysympla import Sympla


@pytest.fixture
def sympla():
    return Sympla("test")
