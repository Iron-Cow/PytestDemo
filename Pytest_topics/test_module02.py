class TestMyTest:  # pytest -v Pytest_topics/test_module02.py::TestMyTest
    def test_type(self):
        assert type(1) == int

    def test_strs(self):
        assert str.upper("python") == "PYTHON"
