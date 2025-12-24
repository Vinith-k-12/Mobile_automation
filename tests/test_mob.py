from pages.login_page import LoginPage
from pages.create_acc import CreateAccountPage
from tests.launch_app import AppLauncher


def test_mob():
    app = AppLauncher()
    driver=app.launch_app()
    login_page = LoginPage(driver)
    login_page.complete_initial_flow()


    

    
    
    # create_account_page = CreateAccountPage(driver)
    # create_account_page.complete_create_account_flow("test", "Hp", "test14@mailsac.com", "Test@1234")




