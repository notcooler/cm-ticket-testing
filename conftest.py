# Pytest configuration
import pytest

def pytest_addoption(parser):
    parser.addoption(
        '--local',
        action='store',
    )

@pytest.fixture
def local(request):
    return request.config.getoption('--local')