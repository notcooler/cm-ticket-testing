from selenium.webdriver.remote.webdriver import WebDriver
from utils.assertion import assert_equal

# Every test needs the driver to be passed to it, type specifiying is not necessary
def run(driver: WebDriver):
    # Arrange
    expectedResult = "Yourticketprovider | Ticketshop"
    actualResult = driver.title

    # Act
    # Run test here, not needed in this case here!

    # Assert
    assert_equal(expectedResult, actualResult, "Title is not correct!")