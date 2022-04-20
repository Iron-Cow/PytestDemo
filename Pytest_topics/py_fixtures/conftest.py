import pytest

pytest.weekdays1 = ['mon', 'tue', 'wed']
pytest.weekdays2 = ['fri', 'sat', 'sun']

def pytest_configure():  # exact name of the function to load variables (run before tests
    pytest.weekdays1 = ['mon', 'tue', 'wed']  # pytest namespece, variables available across all test sessions
    pytest.weekdays2 = ['fri', 'sat', 'sun']

@pytest.fixture(scope="module")
def setup01():
    wk = pytest.weekdays1.copy()
    wk.append("thur")
    yield wk
    print("\n After yield in setup01 fixture \n")

@pytest.fixture
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, "thur")
    yield wk2
    print("\n After yield in setup02 fixture \n")

