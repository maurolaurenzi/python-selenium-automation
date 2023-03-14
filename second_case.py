from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Set up the Selenium client
driver = webdriver.Chrome()

# Test setup
def setup_module(module):
    driver.get('https://proper.ai/')

# Test teardown
def teardown_module(module):
    driver.quit()

# Test case: Verify that contact form is available
def test_contact_form_is_available():
    talk_with_us_btn = driver.find_element(*TALK_WITH_US_BTN)
    talk_with_us_btn.click()
    assert driver.find_element(*FIRST_NAME_INPUT).is_displayed()
    assert driver.find_element(*LAST_NAME_INPUT).is_displayed()
    assert driver.find_element(*EMAIL_INPUT).is_displayed()
    assert driver.find_element(*PHONE_INPUT).is_displayed()
    assert driver.find_element(*DOOR_COUNT_INPUT).is_displayed()

# Test case: Verify that contact form cannot be submitted without name
def test_contact_form_cannot_be_submitted_without_name():
    driver.find_element(*FIRST_NAME_INPUT).send_keys(' ')
    driver.find_element(*LAST_NAME_INPUT).send_keys('Perez')
    driver.find_element(*EMAIL_INPUT).send_keys('jperez@example.com')
    driver.find_element(*PHONE_INPUT).send_keys('123-456-7890')
    driver.find_element(*DOOR_COUNT_INPUT).send_keys('9')
    driver.find_element(*SUBMIT_BTN).click()
    assert not driver.find_element(*SUBMIT_BTN).is_enabled()
    assert driver.find_element(*BLANK_NAME_ERROR).is_displayed()

# Test case: Verify that contact form cannot be submitted without phone number
def test_contact_form_cannot_be_submitted_without_phone_number():
    first_name_input = driver.find_element(*FIRST_NAME_INPUT)
    first_name_input.click()
    first_name_input.send_keys(Keys.END)
    for i in range(len(first_name_input.get_attribute("value"))):
        first_name_input.send_keys(Keys.BACKSPACE)
    first_name_input.send_keys('Juan')
    last_name_input = driver.find_element(*LAST_NAME_INPUT)
    last_name_input.click()
    last_name_input.send_keys(Keys.END)
    for i in range(len(last_name_input.get_attribute("value"))):
        last_name_input.send_keys(Keys.BACKSPACE)
    last_name_input.send_keys('Perez')
    email_input = driver.find_element(*EMAIL_INPUT)
    email_input.click()
    email_input.send_keys(Keys.END)
    for i in range(len(email_input.get_attribute("value"))):
        email_input.send_keys(Keys.BACKSPACE)
    email_input.send_keys('jperez@example.com')
    phone_input = driver.find_element(*PHONE_INPUT)
    phone_input.click()
    phone_input.send_keys(Keys.END)
    for i in range(len(phone_input.get_attribute("value"))):
        phone_input.send_keys(Keys.BACKSPACE)
    phone_input.send_keys('')
    door_count_input = driver.find_element(*DOOR_COUNT_INPUT)
    door_count_input.click()
    door_count_input.send_keys(Keys.END)
    for i in range(len(door_count_input.get_attribute("value"))):
        door_count_input.send_keys(Keys.BACKSPACE)
    door_count_input.send_keys('9')
    driver.find_element(*SUBMIT_BTN).click()
    assert not driver.find_element(*SUBMIT_BTN).is_enabled()
    assert driver.find_element(*BLANK_PHONE_ERROR).is_displayed()




# Test case: Verify that contact form cannot be submitted with invalid phone number
def test_contact_form_cannot_be_submitted_with_invalid_phone_number():
    first_name_input = driver.find_element(*FIRST_NAME_INPUT)
    first_name_input.click()
    first_name_input.send_keys(Keys.END)
    for i in range(len(first_name_input.get_attribute("value"))):
        first_name_input.send_keys(Keys.BACKSPACE)
    first_name_input.send_keys('Juan')
    last_name_input = driver.find_element(*LAST_NAME_INPUT)
    last_name_input.click()
    last_name_input.send_keys(Keys.END)
    for i in range(len(last_name_input.get_attribute("value"))):
        last_name_input.send_keys(Keys.BACKSPACE)
    last_name_input.send_keys('Perez')
    email_input = driver.find_element(*EMAIL_INPUT)
    email_input.click()
    email_input.send_keys(Keys.END)
    for i in range(len(email_input.get_attribute("value"))):
        email_input.send_keys(Keys.BACKSPACE)
    email_input.send_keys('jperez@example.com')
    phone_input = driver.find_element(*PHONE_INPUT)
    phone_input.click()
    phone_input.send_keys(Keys.END)
    for i in range(len(phone_input.get_attribute("value"))):
        phone_input.send_keys(Keys.BACKSPACE)
    phone_input.send_keys('123')
    door_count_input = driver.find_element(*DOOR_COUNT_INPUT)
    door_count_input.click()
    door_count_input.send_keys(Keys.END)
    for i in range(len(door_count_input.get_attribute("value"))):
        door_count_input.send_keys(Keys.BACKSPACE)
    door_count_input.send_keys('9')
    driver.find_element(*SUBMIT_BTN).click()
    assert not driver.find_element(*SUBMIT_BTN).is_enabled()
    assert driver.find_element(*INVALID_PHONE_ERROR).is_displayed()

# Test case: Verify that submit button is available when everything is filled out correctly
def test_submit_button_is_available():
    first_name_input = driver.find_element(*FIRST_NAME_INPUT)
    first_name_input.click()
    first_name_input.send_keys(Keys.END)
    for i in range(len(first_name_input.get_attribute("value"))):
        first_name_input.send_keys(Keys.BACKSPACE)
    first_name_input.send_keys('Juan')
    last_name_input = driver.find_element(*LAST_NAME_INPUT)
    last_name_input.click()
    last_name_input.send_keys(Keys.END)
    for i in range(len(last_name_input.get_attribute("value"))):
        last_name_input.send_keys(Keys.BACKSPACE)
    last_name_input.send_keys('Perez')
    email_input = driver.find_element(*EMAIL_INPUT)
    email_input.click()
    email_input.send_keys(Keys.END)
    for i in range(len(email_input.get_attribute("value"))):
        email_input.send_keys(Keys.BACKSPACE)
    email_input.send_keys('jperez@example.com')
    phone_input = driver.find_element(*PHONE_INPUT)
    phone_input.click()
    phone_input.send_keys(Keys.END)
    for i in range(len(phone_input.get_attribute("value"))):
        phone_input.send_keys(Keys.BACKSPACE)
    phone_input.send_keys('123-456-7890')
    door_count_input = driver.find_element(*DOOR_COUNT_INPUT)
    door_count_input.click()
    door_count_input.send_keys(Keys.END)
    for i in range(len(door_count_input.get_attribute("value"))):
        door_count_input.send_keys(Keys.BACKSPACE)
    door_count_input.send_keys('9')
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(SUBMIT_BTN))
    assert driver.find_element(*SUBMIT_BTN).is_enabled()

