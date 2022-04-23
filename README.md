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

---

## `BDD` - Behaviour Driven Development
`python-bdd`


>Analysts or Prod. owners write scenarios. 

*Feature*: Banking Transactions
>Test pertaining to banking transactions of withdraw and deposit

*Scenario*: Withdrawal of money

>*Given*: Account balance is 100$
> 
>*When*: The Account Holder withdraws 20$
>
>*Then*: The account balance should be 80$

### `Python-BDD` terms and rules:

* `python-dbb` - not stand-alone framework
* Gherkin - `.feature` file
* given, when, then, etc - step included to step definition
* Only 1 feature per `.feature` file
* Multiple scenarios allowed in feature file
* Test modules naming is same as pytest (test_*.py)
* Project structure for `pytest-bdd` is flexible
* Step definition module name can be different to feature file names
* Scenarios **must** be explicitly declared in test modules