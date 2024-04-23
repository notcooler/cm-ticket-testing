# Essentials
print("Importing essentials...")
from utils.loadDriver import loadDriver
import time, json, sys

# Import tests
print("Importing tests...")
from tests import tests

# Load configs
print("Loading configs...")
with open('config.json') as f:
    config = json.load(f)

print("Loading driver...")
runsLocally = False
if len(sys.argv) > 1:
    if sys.argv[1] == "local":
        runsLocally = True
driver = loadDriver(config, runsLocally)

# Initialize element searcher util
from utils.elementSearcher import initialize
initialize(driver, config['searchConfig'])

# Open the page
print("Opening the page...")
driver.get(config['url'])
# Wait for page loading before running tests, TODO: wait until page loaded instead of 5 seconds
print("Waiting for page to load...")
time.sleep(5)

# Run the tests
print("Running tests...")
tests.run_all_tests(driver=driver, url=config['url'])