import pytest


@pytest.mark.skipif(reason="Temp conflict of folders")
def test_argtest01(cmd_opt):
    print("Read config file: " + cmd_opt.readline())
    """
    test_argtest.py::test_argtest01 cmd_opt fixture!
    Read config file: Prod Lab details

    """
    assert 1
