from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_until_element_clickable(driver, element):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element))

def is_displayed(driver, element):
    wait_until_element_clickable(driver, element)
    formElement = driver.find_element(*element)
    return formElement.is_displayed()
