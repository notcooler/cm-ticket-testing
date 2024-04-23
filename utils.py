from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By

from searchConfig import searchConfig

# Initializing
def set_driver(_driver: webdriver.Safari):
    global driver
    driver = _driver

# Element searching
def find_element(key: str, searchParent: WebElement = None):
    if key not in searchConfig:
        raise Exception("The given key was not found in searchconfig! Key: " + key)
    
    # searcher = driver if searchParent is None else searchParent
    searchType: By = SearchTypeStrToType(searchConfig[key]['type'])
    if searchType is None:
        raise Exception("The given type isn't found!")

    return (driver if searchParent is None else searchParent).find_element(searchType, searchConfig[key]['value'])
def find_elements(key: str, searchParent: WebElement = None):
    if key not in searchConfig:
        raise Exception("The given key was not found in searchconfig! Key: " + key)
    
    searcher = driver if searchParent is None else searchParent
    searchType: By = SearchTypeStrToType(searchConfig[key]['type'])
    if searchType is None:
        raise Exception("The given type isn't found!")

    return searcher.find_elements(searchType, searchConfig[key]['value'])

def SearchTypeStrToType(type: str):
    match type:
        case 'ID': return By.ID
        case 'NAME': return By.NAME
        case 'TAG_NAME': return By.TAG_NAME
        case 'CLASS_NAME': return By.CLASS_NAME
        case 'CSS_SELECTOR': return By.CSS_SELECTOR
        case 'LINK_TEXT': return By.LINK_TEXT
        case 'PARTIAL_LINK_TEXT': return By.PARTIAL_LINK_TEXT
        case 'XPATH': return By.XPATH
        case _: return None

# Assertion
def check_assertion(condition, message):
    if not condition:
        raise AssertionError(message)