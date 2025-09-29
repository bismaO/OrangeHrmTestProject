from BaseSeleniumFramework.Utils import config
from OrangeHRMPOM.Application.Login.LoginPage import LoginPage
from conftest import driver


class TestLogin():

    def test_login_with_valid_credentials(self,driver):
        login = LoginPage(driver)
        login.fill_credentials(config.USERNAME,config.PASSWORD)
        login.click_login()

        error = login.get_error_message()
        assert  error == ""
