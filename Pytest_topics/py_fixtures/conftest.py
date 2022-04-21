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

@pytest.fixture()
def setup04(request):
    mon = getattr(request.module, "months") # getting variable from module
    print("\n in Fixture  setup04")
    print("\n Fixture Scope: " + str(request.scope))
    print("\n Calling function: " + str(request.function.__name__))
    print("\n Calling module: " + str(request.module.__name__))
    mon.append("A")

    """
     in Fixture  setup04

     Fixture Scope: function

     Calling function: test_check_request

     Calling module: Pytest_topics.py_fixtures.text_fixtures04
    """

@pytest.fixture()
def setup05():
    def get_structure(name):
        if name == "list":
            return [1, 2, 3]
        elif name == "tuple":
            return (1, 3, 4)

    return get_structure  # return function to use multiple times in one test
