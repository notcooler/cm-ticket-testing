from utils.config import getConfig, getSearchConfig
from utils.driver import loadDriver, getDriverAndLoadPage
from utils.elementSearcher import initialize

def setupTest(isLocal, customUrl: str = None):
    config = getConfig()
    driver = getDriverAndLoadPage(config, isLocal, customUrl)
    initialize(getSearchConfig())
    return driver, config