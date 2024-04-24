from utils.setup import setupTest

# Every test needs the driver to be passed to it, type specifiying is not necessary
def test_run(isLocal):
    driver, config = setupTest(isLocal)

    # Arrange
    expectedResult = "Yourticketprovider | Ticketshop"
    actualResult = driver.title

    # Act
    # Run test here, not needed in this case here!

    # Assert
    assert expectedResult == actualResult, "Title is not correct!"