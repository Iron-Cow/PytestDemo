import pytest


@pytest.fixture
def setup_list():
    city = ["New York", "London", "Riyadh", "Singapore", "Mumbai"]
    return city


def test_get_item(setup_list):
    assert setup_list[0] == "New York"
    assert setup_list[::2] == ["New York", "Riyadh", "Mumbai"]


def test_reverse_list(setup_list):
    assert setup_list[::-2] == ["Mumbai", "Riyadh", "New York"]


@pytest.mark.usefixtures("setup_list")  # alternative way to use fixtures
def test_use_fixture_demo(setup_list):
    assert setup_list[0] == "New York"
