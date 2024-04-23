# Essentials
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time, json

# Import tests
from tests import tests

# Load configs
with open('mainConfig.json') as f:
    config = json.load(f)

# Load driver service
driver_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

# Load driver options
driver_options = Options()
for option in config['browserLaunchOptions']:
    driver_options.add_argument(option)

# Finally load driver with options
driver = webdriver.Chrome(service=driver_service, options=driver_options)

# Set the driver in other needed files
from utils.elementSearcher import set_driver
set_driver(driver)

# Open the page
driver.get(config['url'])
# Wait for page loading before running tests, TODO: wait until page loaded instead of 5 seconds
time.sleep(5)

# Run the tests
tests.run_all_tests(driver=driver, url=config['url'])