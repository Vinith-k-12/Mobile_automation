# import pytest
# from utilities.driver_factory import get_driver

# @pytest.fixture
# def driver():
#     driver = get_driver()
#     yield driver
#     driver.quit()

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.capabilities import desired_caps

@pytest.fixture
def driver():
    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote(
        command_executor="http://localhost:4723",
        options=options
    )
    yield driver
    driver.quit()

    

