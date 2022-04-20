
def test_a1():  # pytest -v Pytest_topics/test_module01.py::test_a1
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 / 5 == 1
    assert 5 * 5 == 25


def test_a2():
    # assert 9/5 == 1.5, "failed test intentionally"
    ...

def test_a3():
    assert 9//5 == 1
