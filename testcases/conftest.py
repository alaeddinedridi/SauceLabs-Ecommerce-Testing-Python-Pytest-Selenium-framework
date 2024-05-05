from selenium import webdriver
import pytest

# Fixtures are used as a common piece of code that we would need to use each time, so to prevent rewriting
# the same code, we just call the same fixture defined here
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()

    driver.maximize_window()
    return driver

# This will return the value of browser from CLI/Hooks
def pytest_addoption(parser):
    parser.addoption("--browser")


# This will return the Browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Pytest HTML report
# it is a hook for adding environment info to HTML report
def pytest_configure(config):
    # config._metadata['Project Name']="SauceLabs"
    # config._metadata['Module Name'] = "Customers"
    # config._metadata['Tester'] = "Aladdin Dridi"
    config._metadata = {
        "Tester": "Aladdin Dridi",
        "Project Name": "SauceLabs ecommerce testing practice",
    }

# this is a hook to delete/modify environment info to HTML report
# @pytest.mark.optionalHook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)