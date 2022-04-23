import pytest
from Pytest_topics.utils.util import get_data

@pytest.mark.parametrize("a,b,c,d", get_data())
def test_check_data_from_file(a, b, c, d):
    assert 1
