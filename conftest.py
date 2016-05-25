# content of conftest.py
import sys
from os.path import dirname, join

sys.path.insert(0, dirname(__file__))


def pytest_addoption(parser):
    parser.addoption("--runslow", action="store_true",
        help="run slow tests")
