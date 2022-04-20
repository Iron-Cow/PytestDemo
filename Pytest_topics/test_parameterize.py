import math
import pytest


@pytest.mark.parametrize("variant", [82, 78, 45, 66])  # multiple options to test
def test_param01(variant):
    assert variant > 33

@pytest.mark.parametrize("inp, out", ([2, 4], [3, 9], [10, 100]))  # multiple parameters
def test_param02(inp, out):
    assert inp ** 2 == out

data = [
    ([2, 3, 4], "sum", 9),
    ([2, 3, 4], "prod", 24),
]

@pytest.mark.parametrize("a,b,c", data)  # multiple parameters
def test_param02(a, b, c):
    if b == "sum":
        assert sum(a) == c
    elif b == "prod":
        assert math.prod(a) == c