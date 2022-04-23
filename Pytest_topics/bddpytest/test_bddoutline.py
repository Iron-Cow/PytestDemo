from pytest_bdd import scenario, given, when, then, parsers
from pathlib import Path

feature_file_dir = "my_features"
feature_file = "scenario_outline.feature"

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(feature_file_dir).joinpath(feature_file)

# scenarios(FEATURE_FILE)

@scenario(FEATURE_FILE, "Scene Outline Test")
def test_outline():
    pass

@given(parsers.parse("There are {start:d} cucumbers"), target_fixture="cucumbers")
def existing_cucumbers(start: int) -> dict:
    return {"start": start}

@when(parsers.parse("I deposit {deposit:d} cucumbers"))
def deposit_cucumbers(cucumbers, deposit):
    cucumbers["start"] += deposit

@when(parsers.parse("I withdraw {withdraw:d} cucumbers"))
def withdraw_cucumbers(cucumbers, withdraw):
    cucumbers["start"] -= withdraw

@then(parsers.parse("I should have {final:d} cucumbers"))
def verify_final_value(cucumbers, final):
    assert cucumbers["start"] == final


