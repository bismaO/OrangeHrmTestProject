from BaseSeleniumFramework.Utils import config
from OrangeHRMPOM.Application.Add_Employee.AddEmployee import AddEmployee
from OrangeHRMPOM.Application.Login.LoginPage import LoginPage
from conftest import driver
import BaseSeleniumFramework.Utils.config
import pytest

class Test_Add_Employee:
    def test_add_employee(self,driver):
        emp = AddEmployee(driver)
        login = LoginPage(driver)
        login.goto()
        login.fill_credentials(config.USERNAME,config.PASSWORD)
        login.click_login()
        emp.navigate_to_pim_menu()



        

