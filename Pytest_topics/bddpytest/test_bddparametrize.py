from pytest_bdd import scenarios, given, when, then, parsers
from pathlib import Path

feature_file_dir = "my_features"
feature_file = "parametrize.feature"

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(feature_file_dir).joinpath(feature_file)

scenarios(FEATURE_FILE)


@given("There are 3 kinds of fruits", target_fixture='fruits')
def existing_fruits():
    fruits = {"apple", "grapes", "melon"}
    return fruits


@when("Add same kind of fruit")
def add_same_fruit(fruits):
    fruits.add("melon")


@then("There is same count of fruit kinds")
def verify_same_fruit_count(fruits):
    assert len(fruits) == 3


@then("If we add a different kind of fruit")
def add_different_fruit(fruits):
    fruits.add("banana")


@then(parsers.parse("The count of kinds increases to {count:d}"))
def different_fruit_count(fruits, count):
    assert len(fruits) == count


@given(parsers.parse("Given {count:d} fruits"), target_fixture='fruit_dict')
def existing_fruits(count):
    fruit_dict = {"have": count, "eat": 0, }
    return fruit_dict


@when(parsers.parse("I eat {eat:d}")) # used for I eat 3/I eat 2 at once
def eat_3_fruits(fruit_dict: dict, eat: int):
    fruit_dict["eat"] += eat
    fruit_dict["have"] -= eat

@then(parsers.parse("I should have {left:d} fruits"))
def verify_resuts(fruit_dict: dict, count, left: int):
    assert count - fruit_dict["eat"] == left
    assert fruit_dict["have"] == left
