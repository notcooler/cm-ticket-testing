# Selenium testing with github actions
__Disclaimer: This project isn't made as a template for easy and quick setup, but for cm.com as a autonomous front-end testing solution thing.__

But if you want to use it for your own use case:
1. Change the url to the url you want to test
2. Clear the ``searchConfig.json`` file, if you want keep the example's. __NOT REQUIRED__
3. The ``tickets/`` folder is really made for that page so you don't need it, but you can keep it as an example. __NOT REQUIRED__

You don't need to change anything on actions side as it should just work.

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

Or you can run it via github actions by running the ``runAllTests`` workflow.

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
__I highly recommend for you to check more example tests first in the ``tests`` folder.__

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

Once again checking the script ``utils/elementSearcher.py`` self is also a really nice and easy way to understand, since it's commented out.

Using the ``find_element(s)`` function isn't required however, but is recommended to use. A good nice complex example of all this combined is in ``tests/totalPriceAmount.py``, and i am guessing it's explained enough.


### That's it, good luck using it. :)
