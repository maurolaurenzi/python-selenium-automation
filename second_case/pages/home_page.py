# page.py
from pages.locators import *

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_contact_form(self):
        talk_with_us_btn = self.driver.find_element(*TALK_WITH_US_BTN)
        talk_with_us_btn.click()

