# page.py
from pages.locators import *
from pages.base_page import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage(BasePage):
    
    # Method to remove any character that the field might have, it returns the input field empty
    def clear_field(self, input_field):
        field = self.driver.find_element(*input_field)
        field.click()
        field.send_keys(Keys.END)
        for i in range(len(field.get_attribute("value"))):
            field.send_keys(Keys.BACKSPACE)
        return field
    
    # Methods to fill the fields: we first clear the field and then send the input
    def fill_first_name_field(self, input):
        first_name = self.clear_field(FIRST_NAME_INPUT)
        first_name.send_keys(input)

    def fill_last_name_field(self, input):
        last_name = self.clear_field(LAST_NAME_INPUT)
        last_name.send_keys(input)
    
    def fill_email_field(self, input):
        email = self.clear_field(EMAIL_INPUT)
        email.send_keys(input)
    
    def fill_phone_field(self, input):
        phone = self.clear_field(PHONE_INPUT)
        phone.send_keys(input)
    
    def fill_door_count_field(self, input):
        door_count = self.clear_field(DOOR_COUNT_INPUT)
        door_count.send_keys(input)

    def select_option(self, input):
        dropdownElement = dropdown_option(input)
        option = self.driver.find_element(*dropdownElement)
        option.click()

    def select_asset_class(self, input):
        asset_btn = self.driver.find_element(*ASSET_CLASS_DROPDOWN)
        asset_btn.click()
        self.select_option(input)
    
    def select_software_used(self, input):
        software_btn = self.driver.find_element(*SOFTWARE_DROPDOWN)
        software_btn.click()
        self.select_option(input)
    
    # Clicking the submit form button
    def submit_form(self):
        submit_btn = self.driver.find_element(*SUBMIT_BTN)
        submit_btn.click()