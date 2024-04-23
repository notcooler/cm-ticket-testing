
# Assertion
def assert_equal(expectedValue, actualValue, message = "No message provided"):
    if expectedValue != actualValue:
        raise AssertionError(message)