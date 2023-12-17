from selenium import webdriver
from pages.locators import *
from pages.home_page import *
from pages.contact_page import *
from tests.commons import *

import json

# Load the test data from the JSON file
with open('data/test_data.json', 'r') as f:
    test_data = json.load(f)

# Extract the data from the JSON object
door_count = test_data['door_count']
email = test_data['email']
first_name = test_data['first_name']
last_name = test_data['last_name']
phone_number = test_data['phone_number']
residential_asset = test_data['residential_asset']
appfolio_software = test_data['appfolio_software']

#Setting up driver and page objects
options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
home_page = HomePage(driver)
contact_page = ContactPage(driver)

# Test setup
def setup_module(module):
    driver.get('https://proper.ai/')
    driver.maximize_window()
    home_page.go_to_contact_form()

# Test teardown
def teardown_module(module):
    driver.quit()

form_elements = [
        FIRST_NAME_INPUT,
        LAST_NAME_INPUT,
        EMAIL_INPUT,
        PHONE_INPUT,
        ASSET_CLASS_DROPDOWN,
        SOFTWARE_DROPDOWN,
        SUBMIT_BTN,
        CLOSE_BTN
    ]

# Test case: Verify that all elements from contact form are displayed
def test_contact_form_is_available():
    for element in form_elements:
        assert is_displayed(driver, element)

# Test case: Verify that contact form cannot be submitted without name
def test_contact_form_cannot_be_submitted_without_name():
    contact_page.fill_last_name_field(last_name)
    contact_page.fill_email_field(email)
    contact_page.fill_phone_field(phone_number)
    contact_page.select_asset_class(residential_asset)
    contact_page.fill_door_count_field(door_count)
    contact_page.select_software_used(appfolio_software)
    # Given there isnt a persistent error message, we validate that the first name field is still displayed after clicking submit
    contact_page.submit_form()
    assert is_displayed(driver, FIRST_NAME_INPUT)

# Test case: Verify that contact form cannot be submitted without door count
def test_contact_form_cannot_be_submitted_without_door_count():
    contact_page.fill_first_name_field(first_name)
    contact_page.fill_first_name_field(last_name)
    contact_page.fill_email_field(email)
    contact_page.fill_phone_field(phone_number)
    contact_page.select_asset_class(residential_asset)
    contact_page.select_software_used(appfolio_software)
    # Given there isnt a persistent error message, we validate that the first name field is still displayed after clicking submit
    contact_page.submit_form()
    assert is_displayed(driver, FIRST_NAME_INPUT)

# Test case: Verify that contact form cannot be submitted without phone number
def test_contact_form_cannot_be_submitted_without_phone_number():
    contact_page.fill_first_name_field(first_name)
    contact_page.fill_first_name_field(last_name)
    contact_page.fill_email_field(email)
    contact_page.select_asset_class(residential_asset)
    contact_page.select_software_used(appfolio_software)
    # Given there isnt a persistent error message, we validate that the first name field is still displayed after clicking submit
    contact_page.submit_form()
    assert is_displayed(driver, FIRST_NAME_INPUT)


