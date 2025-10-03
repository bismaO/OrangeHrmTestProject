from selenium.webdriver.common.by import By
from BaseSeleniumFramework.Helpers.DriverHelper import BasePage
from BaseSeleniumFramework.Utils import config
import pytest_check as check
import uuid

class AddEmployee(BasePage):
    pim_menu = (By.XPATH,"//span[text()='PIM']")
    add_employee_button = (By.XPATH,"//button[text()=' Add ']")
    first_name_input_box = (By.CSS_SELECTOR,"[name='firstName']")
    middle_name_input_box = (By.CSS_SELECTOR,"[name='middleName']")
    last_name_input_box = (By.CSS_SELECTOR,"[name='lastName']")
    profile_image_input_file = (By.CSS_SELECTOR,"input[type='file']")
    save_employee_button = (By.CSS_SELECTOR,"button[type='submit']")
    employee_card_ele = (By.CSS_SELECTOR,".oxd-table-card")
    employee_id_ele = (By.XPATH,".//div/div/div/div/div[2]")
    add_employee_menu = (By.CSS_SELECTOR,"[aria-label='Topbar Menu'] li:nth-of-type(3)")
    create_login_details_toggle_switch = (By.CSS_SELECTOR,"div[class='oxd-switch-wrapper'] span")
    username_input_box = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
    password_input_box = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[4]")
    confirm_password_input_box = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[5]")

    def navigate_to_pim_menu(self):
        self.wait_and_click(self.pim_menu)
        self.wait_for_element_visible(self.add_employee_button)
        check.is_true(self.driver.find_element(*self.add_employee_button).is_displayed())

    def navigate_to_add_employee_menu(self):
        self.wait_and_click(self.add_employee_menu)
        self.wait_for_element_visible(self.first_name_input_box)
        check.is_true(self.driver.find_element(*self.first_name_input_box).is_displayed())

    def add_name(self,firstname = "cleanuptest_" + str(uuid.uuid4().hex[:6]), middlename = None, lastname = None):
        self.wait_and_sendkeys(self.first_name_input_box,firstname)
        self.wait_and_sendkeys(self.middle_name_input_box, middlename)
        self.wait_and_sendkeys(self.last_name_input_box, lastname)
        return firstname + middlename + lastname

    def upload_profile_picture(self,location):
        self.wait_and_sendkeys(self.profile_image_input_file,location)

    def toggle_switch_login_details(self,):
        self.wait_and_click(self.create_login_details_toggle_switch)

    def enter_login_details(self,*,username,password,confirm_password):
        self.wait_and_sendkeys(self.username_input_box, username)
        self.wait_and_sendkeys(self.password_input_box, password)
        self.wait_and_sendkeys(self.confirm_password_input_box, confirm_password)







