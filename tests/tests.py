from selenium.webdriver.remote.webdriver import WebDriver

import tests.example as example
import tests.totalPriceAmount as totalPriceAmount

def discover_tests():
    tests = []

    tests.append(example.run)
    tests.append(totalPriceAmount.run)
    
    return tests

def run_all_tests(driver: WebDriver):
    for test_func in discover_tests():
        print(f"Running test: {test_func.__name__}")
        try:
            test_func(driver)
            print("Test passed.")
        except AssertionError as e:
            print(f"Test failed: {e}")
        except Exception as e:
            print(f"Tests code itself failed: {e}")