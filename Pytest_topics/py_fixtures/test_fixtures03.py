import pytest


def test_del_item(setup01):
    del setup01[-1]
    print(setup01)
    assert setup01 == pytest.weekdays1

def test_remove_item(setup02):
    print(setup02)
    setup02.remove("thur")
    assert setup02 == pytest.weekdays2

"""
pytest -v -k fixtures03 --setup-show 


collected 39 items / 37 deselected / 2 selected                                                                                                                                                                                                                         

Pytest_topics/py_fixtures/test_fixtures03.py::test_del_item 
    SETUP    M setup01
        Pytest_topics/py_fixtures/test_fixtures03.py::test_del_item (fixtures used: setup01)PASSED
Pytest_topics/py_fixtures/test_fixtures03.py::test_remove_item 
        SETUP    F setup02
        Pytest_topics/py_fixtures/test_fixtures03.py::test_remove_item (fixtures used: setup02)PASSED
        TEARDOWN F setup02
    TEARDOWN M setup01
"""