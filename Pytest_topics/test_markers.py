import pytest
# pytest -v -m "smoke"
# module level markers
pytestmark = [pytest.mark.smoke, pytest.mark.strtestmodule]

# pytest -v -m customALALAmarker
# run only test with given marker
@pytest.mark.customALALAmarker
def test_str01():
    assert "aaa"[0] == "a"

@pytest.mark.customALALAmarker
def test_str02():
    assert "aaa"[0] == "a"


# pytest -v -m "customALALAmarker and not strtest"
# pytest -v -m "not strtest"
# run with exclusion
@pytest.mark.customALALAmarker
@pytest.mark.strtest
def test_str03():
    assert "aaa"[0] == "a"

# pytest -v -m "customALALAmarker and strtest"
# when both markers above test

# pytest -v -m "customALALAmarker or strtest"
# any of markers will be fine
@pytest.mark.strtest
def test_str04():
    assert "aaa"[0] == "a"

def test_str05():
    assert "aaa"[0] == "a"


