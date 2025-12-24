from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class LoginPage(BasePage):

    # ===== LOCATORS =====
    allow_button = (By.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
    accept_all_button = (By.XPATH, "//android.widget.Button[@resource-id='consent-accept-all-button']")
    # sign_in_button = (By.ID, "SignInButton")
    continue_as_guest_button = (By.XPATH, "//android.widget.Button[@resource-id='ContinueAsGuestButton']")

    # ===== ACTIONS =====
    def allow_notification(self):
        self.click(self.allow_button)
        print("Notification Allowed")
    # def allow_notification_if_present(self):
    #     try:
    #         self.wait_for_element(self.allow_button, timeout=5)
    #         self.click(self.allow_button)
    #         print("Notification Allowed")
    #     except TimeoutException:
    #         print("Notification dialog not shown")

    def accept_consent(self):
        self.click(self.accept_all_button)
        print("Consent Accepted")

    def click_continue_as_guest(self):
        self.click(self.continue_as_guest_button)
        print("Continued as Guest") 


    # def click_sign_in(self):
    #     self.click(self.sign_in_button)
    #     print("Navigated to Sign In page")

    
    def complete_initial_flow(self):
        self.allow_notification()
        # self.allow_notification_if_present()
        self.accept_consent()
        # self.click_sign_in()
        self.click_continue_as_guest()
        print("Completed Initial Login Flow")
        
