import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# function for extracting the URL of the img element and saving it locally
def download_image(img_element, img_index):
    wait.until(EC.element_to_be_clickable(img_element))
    wait.until(lambda driver: img_element.get_attribute("src").startswith("https:"))
    src_value = img_element.get_attribute("src")

    if src_value and not src_value.startswith("data:"):
        response = requests.get(src_value)
        with open(f"memes/images {img_index+1}.jpg", "wb") as f:
          f.write(response.content)

# function for obtaining the img element after scrolling to it
def obtain_image(image):
    driver.execute_script("arguments[0].scrollIntoView();", image)
    return image.find_element(By.TAG_NAME, "img")

# initializing
driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

# going to website
driver.get("https://icanhas.cheezburger.com/")
driver.maximize_window()

# creating 'memes' folder if it doesn't already exist
if not os.path.exists('memes'):
    os.makedirs('memes')

# obtaining all the posts from the main page
posts = driver.find_elements(By.XPATH,"//*[contains(@class, 'mu-card') and contains(@class, 'mu-z1')]")

# setting the number of images we want to find
num_images = 10

# iterating through the first 10 images and downloading them
for i in range(0,num_images):
  img_element = obtain_image(posts[i])
  try:
    download_image(img_element,i)
  except StaleElementReferenceException:
          # if this excepcion occurs, we need to scroll to the element again and wait for it to be visible
          img_element = obtain_image(posts[i])
          download_image(img_element,i)


