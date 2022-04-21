import os

import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser

QA_config = 'qa.prop'
prod_config = 'prod.prop'


def pytest_addoption(parser: Parser):
    print(parser)
    parser.addoption("--cmdopt")  # pytest -v Pytest_topics/test_argtest.py --cmdopt=Prod


@pytest.fixture
def cmd_opt(pytestconfig: Config):
    print("cmd_opt fixture!")
    opt = pytestconfig.getoption("cmdopt")
    if opt == "Prod":
        f = open(os.path.join(os.path.dirname(__file__), prod_config), "r")
    else:
        f = open(os.path.join(os.path.dirname(__file__), QA_config), "r")
    yield f
