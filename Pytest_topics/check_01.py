# testing pytest.ini # python_files = example_*.py test*.py check_*.py
def test_01():
    assert 1


# testing pytest.ini # python_functions = test* *_test check*
def check01():
    assert 1
