# Pytest configuration
import pytest

def pytest_addoption(parser):
    parser.addoption(
        '--isLocal',
        action='store',
    )

@pytest.fixture
def isLocal(request):
    isLocal = request.config.getoption('--isLocal')
    return isLocal == 'true' if isLocal else False