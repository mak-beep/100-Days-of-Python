from selenium import webdriver
# To search elements
from selenium.webdriver.common.by import By
# To press buttons
from selenium.webdriver.common.keys import Keys

URL = "FORM-URL"

driver = webdriver.Chrome()

driver.get(url=URL)

first_name = driver.find_element(by=By.NAME, value="fName")
first_name.send_keys("Moaaz")
last_name = driver.find_element(by=By.NAME, value="lName")
last_name.send_keys("Ahmad")
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("moaazahmad@mail.com")

submit = driver.find_element(by=By.CSS_SELECTOR, value="form button")
submit.click()

while True:
    pass