import pytest


def test_strjoin():  # PASSED
    s1 = "Python,Pytest and Automation"
    l1 = ["Python,Pytest", "and", "Automation"]
    l2 = ["Python", "Pytest and Automation"]
    assert " ".join(l1) == s1


@pytest.mark.xfail(raises=IndexError)  # if wrong error expected - test will be failed, if correct - XFAIL
def test_str01():  # XFAIL
    letters = "abc"
    assert letters[100]

def old_func():
    return False


@pytest.mark.xfail(old_func() == False, reason="Known Issue, function does not working fine (should return True)")
def test_str02(): # XFAIL
    assert old_func() == True

@pytest.mark.xfail(old_func() == False, reason="Known Issue, function does not working fine (should return True)")
def test_str03(): # XPASS (supposed to be failed, but passed)
    assert old_func() == False


# Pytest_topics/test_xfail.py::test_strjoin PASSED                                                                                                                                                                                                                  [ 68%]
# Pytest_topics/test_xfail.py::test_str01 XFAIL                                                                                                                                                                                                                     [ 72%]
# Pytest_topics/test_xfail.py::test_str02 XFAIL (Known Issue, function does not working fine (should return True))                                                                                                                                                  [ 76%]
# Pytest_topics/test_xfail.py::test_str03 XPASS (Known Issue, function does not working fine (should return True))
