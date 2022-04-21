`Fixtures` - functions that are run by pytest before (and sometimes after) the actual test functions.
Eg. setup DB connection, initialize webdriver ect.

We can put fixtures in individual test files, or in `conftest.py` for marking fixtures available in multiple test files.

`conftest.py` can be in multiple versions for different subdirectories.

It should **not** be imported by test files


### Fixture scopes:

Fixtures are created when firs requested by a test and are destroyed based on their scope:

* `function`: the default scope, the fixture is destoyed at the end of the test.
* `class`: the fixture is destroyed during teardown of the last test in the class
* `module`: the fixture is destroyed during teardown of the last test in the module
* `package`: the fixture is destroyed during teardown of the last test in the package
* `session`: the fixture is destroyed at the end of the test session
