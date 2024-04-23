from selenium.webdriver.remote.webdriver import WebDriver
from utils.assertion import assert_equal

# Every test needs the driver to be passed to it, type specifiying is not necessary
def run(driver: WebDriver):
    assert_equal(True, False, "It was destined for this test to fail.")