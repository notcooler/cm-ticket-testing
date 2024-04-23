from selenium import webdriver
import time

# Load driver and set it in other needed
driver = webdriver.Safari()
from utils import set_driver
set_driver(driver)

# Import tests
from tests import tests

config = {
    "url": "https://shop.yourticketprovider.nl/?productid=3ba44a39-1393-e9b6-f30e-25b5c61a6482&_ga=2.158438847.483138645.1713773460-927077746.1713773459",
}
driver.get(config['url'])

# Wait for loading
time.sleep(5) #todo: actually wait until fully loaded instead of 3 seconds

# Run the tests
tests.run_all_tests(driver=driver)