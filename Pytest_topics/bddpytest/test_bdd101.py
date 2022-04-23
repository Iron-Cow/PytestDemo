import pytest
from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path

feature_file_dir = "my_features"
feature_file = "first101.feature"

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(feature_file_dir).joinpath(feature_file)


def pytest_configure():  # make it global
    pytest.AMT = 0


scenarios(FEATURE_FILE)  # alternative to single scenarios (commented)


# @scenario(FEATURE_FILE, "Withdrawal of money")
# def test_withdrawal():  # test_bdd101.py::test_withdrawal <- venv/lib/python3.8/site-packages/pytest_bdd/scenario.py End of Withdrawal test
#     print("End of Withdrawal test")


@given("The account is 100")
def current_balance():
    pytest.AMT = 100


@when("The account holder withdraws 30")
def withdraw_amount():
    pytest.AMT -= 30


@then("The account balance should be 70")
def final_balance():
    assert pytest.AMT == 70


###


# @scenario(FEATURE_FILE, "Removal of items from set")
# def test_removal_of_set_items():
#     print("End of removing test")


@given("A set of 3 fruits", target_fixture="my_set")  # returns value, works as fixture for next steps
def current_balance():
    my_set = {"apple", "banana", "cherry"}
    return my_set


@when("Remove a fruit from the set")
def remove_fruit(my_set: set):
    my_set.pop()
    print(f"myset after removing - {my_set}")


@then("The set will have 2 fruits")
def final_set(my_set):
    assert len(my_set) == 2

# test_bdd101.py::test_withdrawal <- venv/lib/python3.8/site-packages/pytest_bdd/scenario.py
# test_bdd101.py::test_removal_of_set_items <- venv/lib/python3.8/site-packages/pytest_bdd/scenario.py