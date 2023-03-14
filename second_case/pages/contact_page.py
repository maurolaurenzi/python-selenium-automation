# page.py
from pages.locators import *
from pages.base_page import *
from selenium.webdriver.common.keys import Keys

class ContactPage(BasePage):
    def first_name_input_is_displayed(self):
        first_name = self.driver.find_element(*FIRST_NAME_INPUT)
        return first_name.is_displayed()
    
    def last_name_input_is_displayed(self):
        last_name = self.driver.find_element(*LAST_NAME_INPUT)
        return last_name.is_displayed()
    
    def email_input_is_displayed(self):
        email = self.driver.find_element(*EMAIL_INPUT)
        return email.is_displayed()
    
    def phone_input_is_displayed(self):
        phone = self.driver.find_element(*PHONE_INPUT)
        return phone.is_displayed()
    
    def door_count_is_displayed(self):
        door_count = self.driver.find_element(*EMAIL_INPUT)
        return door_count.is_displayed()
    
    def clear_field(self, input_field):
        field = self.driver.find_element(*input_field)
        field.click()
        field.send_keys(Keys.END)
        for i in range(len(field.get_attribute("value"))):
            field.send_keys(Keys.BACKSPACE)
        return field
    
    #For the "fill" methods, we first clear the field and then send the input
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
    
    def enter_name_error_is_displayed(self):
        return self.driver.find_element(*BLANK_NAME_ERROR).is_displayed()
    
    def enter_phone_error_is_displayed(self):
        return self.driver.find_element(*BLANK_PHONE_ERROR).is_displayed()
    
    def invalid_phone_error_is_displayed(self):
        return self.driver.find_element(*INVALID_PHONE_ERROR).is_displayed()
    
    def submit_button_is_enabled(self):
        return self.driver.find_element(*SUBMIT_BTN).is_enabled()