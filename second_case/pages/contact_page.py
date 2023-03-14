# page.py
from pages.locators import *
from selenium.webdriver.common.keys import Keys

class ContactPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_contact_form(self):
        talk_with_us_btn = self.driver.find_element(*TALK_WITH_US_BTN)
        talk_with_us_btn.click()

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
    
    #For the "fill" methods, we first clear the field and then send the input
    def fill_first_name_field(self, input):
        first_name = self.driver.find_element(*FIRST_NAME_INPUT)
        first_name.click()
        first_name.send_keys(Keys.END)
        for i in range(len(first_name.get_attribute("value"))):
            first_name.send_keys(Keys.BACKSPACE)
        first_name.send_keys(input)

    def fill_last_name_field(self, input):
        last_name = self.driver.find_element(*LAST_NAME_INPUT)
        last_name.click()
        last_name.send_keys(Keys.END)
        for i in range(len(last_name.get_attribute("value"))):
            last_name.send_keys(Keys.BACKSPACE)
        last_name.send_keys(input)
    
    def fill_email_field(self, input):
        email = self.driver.find_element(*EMAIL_INPUT)
        email.click()
        email.send_keys(Keys.END)
        for i in range(len(email.get_attribute("value"))):
            email.send_keys(Keys.BACKSPACE)
        email.send_keys(input)
    
    def fill_phone_field(self, input):
        phone = self.driver.find_element(*PHONE_INPUT)
        phone.click()
        phone.send_keys(Keys.END)
        for i in range(len(phone.get_attribute("value"))):
            phone.send_keys(Keys.BACKSPACE)
        phone.send_keys(input)
    
    def fill_door_count_field(self, input):
        door_count = self.driver.find_element(*DOOR_COUNT_INPUT)
        door_count.click()
        door_count.send_keys(Keys.END)
        for i in range(len(door_count.get_attribute("value"))):
            door_count.send_keys(Keys.BACKSPACE)
        door_count.send_keys(input)
    
    def enter_name_error_is_displayed(self):
        return self.driver.find_element(*BLANK_NAME_ERROR).is_displayed()
    
    def enter_phone_error_is_displayed(self):
        return self.driver.find_element(*BLANK_PHONE_ERROR).is_displayed()
    
    def invalid_phone_error_is_displayed(self):
        return self.driver.find_element(*INVALID_PHONE_ERROR).is_displayed()
    
    def submit_button_is_enabled(self):
        return self.driver.find_element(*SUBMIT_BTN).is_enabled()