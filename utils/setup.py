from utils.config import getConfig, getSearchConfig
from utils.driver import loadDriver, getDriverAndLoadPage
from utils.elementSearcher import initialize

def setupTest(local, customUrl: str = None):
    config = getConfig()
    print(local)
    driver = getDriverAndLoadPage(config, local != None, customUrl)
    initialize(getSearchConfig())
    return driver, config