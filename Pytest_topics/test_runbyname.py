
# pytest -v -k "byname" --tb=no
# run tests with module name containing "byname" keyword (without traceback)

# pytest - v - k "byname and xfail" - -tb = no
# pytest - v - k "byname or not module" - -tb = no

def test_runbyname():
    assert 1 != 0


def test_run_by_name():
    assert 1 != 0