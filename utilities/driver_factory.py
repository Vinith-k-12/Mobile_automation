from appium import webdriver
from config.capabilities import desired_caps

def get_driver():
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723/wd/hub",
        desired_capabilities=desired_caps
    )
    driver.implicitly_wait(10)
    return driver
