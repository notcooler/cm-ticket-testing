
# Assertion
def assert_equal(expectedValue, actualValue, message = "No message provided"):
    if expectedValue != actualValue:
        # Possible add code here to send test results to somewhere else, e.g. asure devops.
        raise AssertionError(message)