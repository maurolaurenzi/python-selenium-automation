from selenium.webdriver.common.by import By

# Talk with us button
TALK_WITH_US_BTN = (By.XPATH,"//div[@class='nav-col-small side-col']//div[contains(text(),'Talk With Us')]")

# First name input field
FIRST_NAME_INPUT = (By.ID,"firstname")

# Last name input field
LAST_NAME_INPUT = (By.ID, "lastname")

# Email input field
EMAIL_INPUT = (By.ID, "email")

# Phone input field
PHONE_INPUT = (By.ID, "phone")

# Asset class field
ASSET_CLASS_DROPDOWN = (By.ID, "asset-class")

# Door count field
DOOR_COUNT_INPUT = (By.ID, "Door-Count")

# Used software field
SOFTWARE_DROPDOWN = (By.XPATH, "//*[@id='software_1__c']")

# Submit button
SUBMIT_BTN = (By.XPATH,"//input[@type='submit']")

# Close form button
CLOSE_BTN = (By.XPATH,"//a[contains(text(),'X Close Form')]")

def dropdown_option(value):
    asset_option = (By.XPATH, f"//option[@value='{value}']")
    return asset_option