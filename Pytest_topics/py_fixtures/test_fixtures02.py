import os

import pytest

weekdays1 = ['mon', 'tue', 'wed']
weekdays2 = ['fri', 'sat', 'sun']

filename = "file1.txt"

@pytest.fixture
def setup01():
    weekdays1.append("thur")
    yield weekdays1
    print("\n After yield in setup01 fixture \n")
    weekdays1.pop()

@pytest.fixture
def setup02():
    weekdays2.insert(0, "thur")
    yield weekdays2
    print("\n After yield in setup02 fixture \n")
    weekdays1.pop()
    print(weekdays1)

@pytest.fixture()
def setup03():
    f = open(filename, "w")
    f.write("Pytest demo file")
    f.close()
    f = open(filename, "r+")
    yield f
    f.close()  # actions after test execution
    os.remove(filename)


def test_extend_list(setup01):
    setup01.extend(weekdays2)
    assert setup01 == ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']
    print("test end")


def test_len(setup01, setup02):
    assert len(weekdays1 + setup02) == len(setup01 + weekdays2)

def test_filetest(setup03):
    assert (setup03.readline()) == "Pytest demo file"