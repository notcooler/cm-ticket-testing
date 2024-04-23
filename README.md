# Selenium testing for front-end with github actions
_This project isn't made as a template for someone to use, but for cm.com. But I have coded it pretty generic enough so it may be possible to use it as a template._

## Setup
Clone the repository and make sure you have chrome installed, install dependencies using: 
```
pip3 install -r requirements.txt
```

To run the tests, run:
```sh
python3 main.py local
```
If you are running it on your local computer, make sure to add the ``local`` argument to it. This makes sure no new chrome is installed and is easier to use. Without the local argument the code may assume it's running on actions. Check ``utils/loadDriver.py`` for further info.

# Make your own test
A barebones test should have atleast one test function where only one argument takes place named driver.
Here is an example of an button clicking test.
```py
from selenium.webdriver.remote.webdriver import WebDriver
from utils.assertion import assert_equal
from utils.elementSearcher import find_elements


# Every test needs the driver to be passed to it, type specifiying is not necessary
def run(driver: WebDriver):
    # Arrange
    expectedClicks = randint(1, 10)
    buttons = find_elements('buttons')

    # Act
    clickButtons(buttons, expectedClicks)

    # Assert
    actualClicks = getClickedButtonCounter()
    assert_equal(expectedClicks, actualClicks, f"Not enough buttons clicked! Missing {expectedClicks - actualClicks} clicks...")
```
I highly recommend for you to check more example tests first in the ``tests`` folder.

## How to use find_element(s) function
The function takes 2 arguments, one called key which gets searched in the ``configs/searchConfig.json`` file.
Every key has a an type and value attached to it like this:
```json
{
    "key": {
        "type": "type",
        "value": "value"
    },
    "otherKey": {
        "type": "XPATH",
        "value": "./div/div/div[2]/div[2]"
    },
}
```
Once the key gets fetched it calls the ``searcher.find_element or find_elements`` function and passes the type and value argument to it.
This approach makes it more easy it find elements to intereact with them.
And makes it more generic since all tests can access the ``find_element(s)`` function and it's config is easily changeable without touching the code.

The second argument ``parentElement`` isn't required and if it's given it will search from the perspective of the parent and not from the beginning of the page, really usefull.

Using the ``find_element(s)`` function isn't required however, but is recommended to use. A good nice complex example of all this combined is in ``tests/totalPriceAmount.py``, and i am guessing it's explained enough.
