# Essentials
print("Importing essentials...")
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.core.utils import read_version_from_cmd
from webdriver_manager.core.os_manager import PATTERN
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time

def loadDriver(config, runsLocally = False):
    if runsLocally:
        return webdriver.Chrome()
    
    # Load driver service
    driver_version = read_version_from_cmd('/usr/bin/chromium --version', PATTERN[ChromeType.CHROMIUM])
    print("Loading driver, version: " + driver_version)
    driver_service = Service(ChromeDriverManager(driver_version=driver_version, chrome_type=ChromeType.CHROMIUM).install())

    # Load driver options
    print("Loading driver options...")
    driver_options = Options()
    for option in config['browserLaunchOptions']:
        driver_options.add_argument(option)

    # Finally load driver with options
    return webdriver.Chrome(service=driver_service, options=driver_options)

def getDriverAndLoadPage(config, runsLocally, customUrl:str = None):
    driver = loadDriver(config, runsLocally)
    driver.get(customUrl if customUrl else config['url']) # Use custom url if provided, otherwise use the default one
    time.sleep(config['waitPageLoadDelay']) # Wait for page to load
    return driver