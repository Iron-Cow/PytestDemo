`Fixtures` - functions that are run by pytest before (and sometimes after) the actual test functions.
Eg. setup DB connection, initialize webdriver ect.

We can put fixtures in individual test files, or in `conftest.py` for marking fixtures available in multiple test files.

