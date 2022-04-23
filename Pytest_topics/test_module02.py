class TestMyTestSuite:  # pytest -v Pytest_topics/test_module02.py::TestMyTestSuite
    def test_type(self):
        assert type(1) == int

    def test_strs(self):
        assert str.upper("python") == "PYTHON"

class TestMyTestWrongEnding:
    def test_type(self):
        assert type(1) == int

    def test_strs(self):
        assert str.upper("python") == "PYTHON"
