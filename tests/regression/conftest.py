try:
    import ConfigParser as configparser
except ImportError:
    import configparser
import os
import pytest


def pytest_addoption(parser):
    parser.addoption('--config', action='store', default='3.0-nginx')


@pytest.fixture(scope='session')
def config(request):
    cp = configparser.RawConfigParser()
    cp.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    return dict(cp.items(request.config.getoption('--config')))
