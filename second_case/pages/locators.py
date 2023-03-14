from selenium.webdriver.common.by import By

# Talk with us button
TALK_WITH_US_BTN = (By.XPATH,"//nav/div/div/button")

# First name input field
FIRST_NAME_INPUT = (By.XPATH,"//form/div[1]/div/div[1]/input")

# Last name input field
LAST_NAME_INPUT = (By.XPATH, "//form/div[2]/div/div[1]/input")

# Email input field
EMAIL_INPUT = (By.NAME, "email")

# Phone input field
PHONE_INPUT = (By.NAME, "phone")

# Units input field
DOOR_COUNT_INPUT = (By.NAME, "units")

# Submit button
SUBMIT_BTN = (By.XPATH,"//form/div[6]/div/button")

# Enter name error message
BLANK_NAME_ERROR = (By.XPATH,"//div/span[text()=\"Please enter first name\"]")

# Enter phone error message
BLANK_PHONE_ERROR = (By.XPATH,"//div/span[text()=\"Please enter phone number\"]")

# Blank door count error message
BLANK_DOOR_COUNT_ERROR = (By.XPATH,"//div/span[text()=\"Please complete this required field\"]")

# Invalid phone error message
INVALID_PHONE_ERROR = (By.XPATH,"//div/span[text()=\"Please enter valid phone number\"]")