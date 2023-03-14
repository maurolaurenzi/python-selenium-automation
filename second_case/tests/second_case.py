from selenium import webdriver
from pages.locators import *
from pages.home_page import *
from pages.contact_page import *
import json

# Load the test data from the JSON file
with open('data/test_data.json', 'r') as f:
    test_data = json.load(f)

# Extract the data from the JSON object
blank_value = test_data['blank_value']
door_count = test_data['door_count']
email = test_data['email']
first_name = test_data['first_name']
invalid_phone_number = test_data['invalid_phone_number']
last_name = test_data['last_name']
phone_number = test_data['phone_number']

#Setting up driver and page objects
driver = webdriver.Chrome()
home_page = HomePage(driver)
contact_page = ContactPage(driver)

# Test setup
def setup_module(module):
    driver.get('https://proper.ai/')
    home_page.go_to_contact_form()

# Test teardown
def teardown_module(module):
    driver.quit()

# Test case: Verify that contact form is available
def test_contact_form_is_available():
    assert contact_page.first_name_input_is_displayed()
    assert contact_page.last_name_input_is_displayed()
    assert contact_page.email_input_is_displayed()
    assert contact_page.phone_input_is_displayed()
    assert contact_page.door_count_input_is_displayed()

# Test case: Verify that contact form cannot be submitted without name
def test_contact_form_cannot_be_submitted_without_name():
    contact_page.fill_first_name_field(blank_value)
    contact_page.fill_last_name_field(last_name)
    contact_page.fill_email_field(email)
    contact_page.fill_phone_field(phone_number)
    contact_page.fill_door_count_field(door_count)

    assert not contact_page.submit_button_is_enabled()
    assert contact_page.enter_name_error_is_displayed()

# Test case: Verify that contact form cannot be submitted without door count
def test_contact_form_cannot_be_submitted_without_phone_number():
    contact_page.fill_first_name_field(first_name)
    contact_page.fill_first_name_field(last_name)
    contact_page.fill_email_field(email)
    contact_page.fill_phone_field(phone_number)
    contact_page.fill_door_count_field(blank_value)
    assert not contact_page.submit_button_is_enabled()
    assert contact_page.blank_door_count_error_is_displayed()

# Test case: Verify that contact form cannot be submitted without phone number
def test_contact_form_cannot_be_submitted_without_phone_number():
    contact_page.fill_first_name_field(first_name)
    contact_page.fill_first_name_field(last_name)
    contact_page.fill_email_field(email)
    contact_page.fill_phone_field(blank_value)
    contact_page.fill_door_count_field(door_count)
    assert not contact_page.submit_button_is_enabled()
    assert contact_page.enter_phone_error_is_displayed()

# Test case: Verify that contact form cannot be submitted with invalid phone number
def test_contact_form_cannot_be_submitted_with_invalid_phone_number():
    contact_page.fill_first_name_field(first_name)
    contact_page.fill_first_name_field(last_name)
    contact_page.fill_email_field(email)
    contact_page.fill_phone_field(invalid_phone_number)
    contact_page.fill_door_count_field(door_count)
    assert not contact_page.submit_button_is_enabled()
    assert contact_page.invalid_phone_error_is_displayed()

# Test case: Verify that submit button is available when everything is filled out correctly
def test_submit_button_is_available():
    contact_page.fill_first_name_field(first_name)
    contact_page.fill_first_name_field(last_name)
    contact_page.fill_email_field(email)
    contact_page.fill_phone_field(phone_number)
    contact_page.fill_door_count_field(door_count)
    assert contact_page.submit_button_is_enabled()

