import sys
import pytest

pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="Skip due to run on windows")


const = 9 / 5


def cels_to_fah(cels=0):
    fah = (cels * const) + 32
    return fah


@pytest.mark.skip(reason="Skip for no reason specified")
def test_case01():
    assert type(const) == float


@pytest.mark.skipif(sys.version_info > (3, 7), reason="Does not work on py version above 3.7")
def test_case02():
    assert cels_to_fah() == 32


@pytest.mark.skipif(sys.version_info > (3, 7), reason="Does not work on py version above 3.7")
def test_case03():
    assert cels_to_fah() == 32


def test_case04():
    assert cels_to_fah(38) == 100.4
