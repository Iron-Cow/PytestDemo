import pytest
from _pytest.fixtures import SubRequest


# fixtures
@pytest.fixture(params=[(3, 4), [3, 5]], ids=["tuple_tttest", "list_tttest"])
def fixture01(request: SubRequest):
    return request.param  # parametrization from fixture


@pytest.fixture(params=["access", "len", "assign", "pass"])
def fixture02(request: SubRequest):
    return request.param


# tests
def test_param_fixture01(fixture01):
    assert (type(fixture01) in [tuple, list])

    # test names also came from ids:
    '''
    test_fixtures05.py::test_param_fixture01[tuple_tttest] PASSED              [ 50%]
    test_fixtures05.py::test_param_fixture01[list_tttest] PASSED               [100%]
    '''


def test_param_fixture02(fixture01, fixture02):  # relations between multiple parametrizing fixtures
    if fixture02 == "access":
        assert fixture01[0] > 0
    elif fixture02 == "len":
        assert len(fixture01)
    elif fixture02 == "assign":
        if type(fixture01) == tuple:
            with pytest.raises(TypeError):
                fixture01[0] = 99
        else:
            fixture01[0] = 99
            assert 1
    else:
        assert 1

    """
    test_fixtures05.py::test_param_fixture02[tuple_tttest-access] PASSED     [ 12%]
    test_fixtures05.py::test_param_fixture02[tuple_tttest-len] PASSED        [ 25%]
    test_fixtures05.py::test_param_fixture02[tuple_tttest-assign] PASSED     [ 37%]
    test_fixtures05.py::test_param_fixture02[tuple_tttest-pass] PASSED       [ 50%]
    test_fixtures05.py::test_param_fixture02[list_tttest-access] PASSED      [ 62%]
    test_fixtures05.py::test_param_fixture02[list_tttest-len] PASSED         [ 75%]
    test_fixtures05.py::test_param_fixture02[list_tttest-assign] PASSED      [ 87%]
    test_fixtures05.py::test_param_fixture02[list_tttest-pass] PASSED        [100%]
    """
