# page.py
from pages.locators import *
from pages.base_page import *

class HomePage(BasePage):
    def go_to_contact_form(self):
        talk_with_us_btn = self.driver.find_element(*TALK_WITH_US_BTN)
        talk_with_us_btn.click()

