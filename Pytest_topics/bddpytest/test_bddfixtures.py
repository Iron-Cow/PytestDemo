import pytest
from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path

feature_file_dir = "my_features"
feature_file = "fixtures.feature"

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(feature_file_dir).joinpath(feature_file)

scenarios(FEATURE_FILE)

@pytest.fixture()
def setup_set() -> set:
    print("\n In fixture... setup_set() function.. \n")
    countries = {"Poland", "USA", "Israel", "Germany", "Ukraine"}
    return countries


@given("A data type set")
def check_set_type(setup_set):
    print("In background check data type")
    if not isinstance(setup_set, set):
        pytest.xfail("The type is not set type")


@given("The set is not empty")
def check_set_not_empty(setup_set: set):
    print("In background check not empty set")
    if len(setup_set) == 0:
        pytest.xfail("The set of elements are empty")


@given("A sent with 3 elements", target_fixture="setup_set1")
def set_of_elems(setup_set: set):
    if len(setup_set) == 0:
        pytest.xfail("The set of elements are empty")

    while len(setup_set) > 3:
        setup_set.pop()

    return setup_set


@when("Add 2 elents to the set")
def add_elements(setup_set1: set):
    setup_set1.add("India")
    setup_set1.add("Australia")


@then("The set should have 5 elements")
def final_set_elements(setup_set1: set):
    assert len(setup_set1) == 5
