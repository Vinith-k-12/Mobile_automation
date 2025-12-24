from appium import webdriver
from config.capabilities import desired_caps
from appium.options.android import UiAutomator2Options
class AppLauncher:

    def launch_app(self):
        server_url = "http://localhost:4723"
        
        options_app = UiAutomator2Options()
        options_app.platformName = "Android"
        options_app.platformVersion = 16
        options_app.deviceName = "Pixel 7a"
        options_app.set_capability("udid", "emulator-5554")
        options_app.automationName = "UiAutomator2"
        options_app.set_capability("noReset", True)
        options_app.set_capability("appPackage", "com.hp.printercontrol")
        options_app.set_capability("appActivity", "com.hp.printercontrol.hpx.PrinterControlWrapperActivity")
        # options_app.set_capability("forceAppLaunch", True)
        # Wait for any activity
        options_app.set_capability("autoGrantPermissions", True)
        options_app.set_capability("appWaitActivity", "*")
        options_app.set_capability("appWaitDuration", 60000)

        driver = webdriver.Remote(
            command_executor=server_url,    
            options=options_app
        )
        return driver
