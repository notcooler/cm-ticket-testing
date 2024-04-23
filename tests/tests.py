from selenium.webdriver.remote.webdriver import WebDriver
import time

import tests.example as example
import tests.totalPriceAmount as totalPriceAmount

def discover_tests():
    tests = []
    
    # Add all test functions here
    tests.append(example.run)
    tests.append(totalPriceAmount.run)
    
    return tests

def run_all_tests(driver: WebDriver, url: str):
    for test_func in discover_tests():
        print(f"------------------\nRunning test: {test_func.__module__}")
        try:
            test_func(driver)
            print("Test passed.")
        except AssertionError as e:
            print(f"Test failed: {e}")
        except Exception as e:
            print(f"Test\'s code itself failed: {e}")
        
        # Refresh the page to start the next test
        driver.get(url=url + "&cacheBuster=" + str(time.time()))
        time.sleep(3) # wait until page refreshed