from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage

class CreateAccountPage(BasePage):

    # ===== LOCATORS =====

    create_account_button = (By.ID, "sign-up")
    first_name_field = (By.ID, "firstName")
    last_name_field = (By.ID, "lastName")
    email_field = (By.ID, "email")
    password_field = (By.ID, "password")


    # ===== ACTIONS =====

    def click_create_account(self):
        self.click(self.create_account_button)
        print("Navigated to Create Account page")

    def text_first_name(self, first_name):
        first_name_field = (By.ID, "firstName")
        self.driver.find_element(*first_name_field).send_keys("test")
        print(f"Entered First Name: {first_name}")

    def text_last_name(self, last_name):
        last_name_field = (By.ID, "lastName")
        self.driver.find_element(*last_name_field).send_keys("Hp")
        print(f"Entered Last Name: {last_name}")

    def text_email(self, email):
        email_field = (By.ID, "email")
        self.driver.find_element(*email_field).send_keys("test14@mailsac.com")
        print(f"Entered Email: {email}")

    def text_password(self, password):
        password_field = (By.ID, "password")
        self.driver.find_element(*password_field).send_keys("Test@1234")
        print(f"Entered Password: {password}")
    
    def complete_create_account_flow(self, first_name, last_name, email, password):
        self.click_create_account()
        self.text_first_name(first_name)
        self.text_last_name(last_name)
        self.text_email(email)
        self.text_password(password)
        print("Completed Create Account flow")

