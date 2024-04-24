from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

# Initializing
def initialize(_searchConfig: dict):
    global searchConfig
    searchConfig = _searchConfig

# Element searching
def findElement(key: str, searcher: WebElement | WebDriver):
    # Check if the key is in searchConfig
    if key not in searchConfig:
        raise Exception("The given key was not found in searchconfig! Key: " + key)

    # Get the search type and value
    searchType: By = searchTypeStrToType(searchConfig[key]['type'])
    if searchType is None:
        raise Exception("The given type isn't found!")

    # Finally search for the element
    return searcher.find_element(searchType, searchConfig[key]['value'])

def findElements(key: str, searcher: WebElement | WebDriver):
    # Check if the key is in searchConfig
    if key not in searchConfig:
        raise Exception("The given key was not found in searchconfig! Key: " + key)

    # Get the search type and value
    searchType: By = searchTypeStrToType(searchConfig[key]['type'])
    if searchType is None:
        raise Exception("The given type isn't found!")

    # Finally search for the element
    return searcher.find_elements(searchType, searchConfig[key]['value'])

def searchTypeStrToType(type: str):
    match type:
        case 'ID': return By.ID # Find element by ID
        case 'NAME': return By.NAME # Find element by name e.g. name="value"
        case 'TAG_NAME': return By.TAG_NAME # Find element by tag name e.g. <div>
        case 'CLASS_NAME': return By.CLASS_NAME # Find element by class name e.g. class="value"
        case 'CSS_SELECTOR': return By.CSS_SELECTOR # Find element by css selector e.g. #value
        case 'LINK_TEXT': return By.LINK_TEXT # Find element by link text e.g. <a>text</a>
        case 'PARTIAL_LINK_TEXT': return By.PARTIAL_LINK_TEXT # Find element by partial link text e.g. <a>text</a>
        case 'XPATH': return By.XPATH # Find element by xpath
        case _: return None # Return None if the type isn't found, results in a throw of an exception