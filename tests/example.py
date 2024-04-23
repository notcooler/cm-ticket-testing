from selenium.webdriver.remote.webdriver import WebDriver
from utils.assertion import assert_equal

def run(driver: WebDriver):
    assert_equal("Yourticketprovider | Ticketshop", driver.title, "Title is not correct!")