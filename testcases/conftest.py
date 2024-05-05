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
        driver = webdriver.Chrome()
        #driver = webdriver.Edge()

    driver.maximize_window()
    return driver

# This will return the value of browser from CLI/Hooks
def pytest_addoption(parser):
    parser.addoption("--browser")


# This will return the Browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")