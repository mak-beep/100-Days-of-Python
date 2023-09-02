from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
URL = "https://tinder.com/"

driver = webdriver.Chrome()

driver.get(url=URL)
sleep(15)
log_in_button = driver.find_element(by=By.XPATH, value="//*[@id='u-1535117240']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]")
log_in_button.click()
sleep(5)
google_sign_in = driver.find_element(by=By.XPATH, value="//*[@id='u1031468980']/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[1]")
google_sign_in.click()
sleep(5)
base_window = driver.window_handles[0]
google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)
email_field = driver.find_element(by=By.NAME, value="identifier")
email_field.send_keys(EMAIL)

next_button = driver.find_element(by=By.ID, value="identifierNext")
next_button.click()
sleep(5)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(PASSWORD)

driver.switch_to.window(base_window)

while True:
    try:
        like_button = driver.find_element(by=By.XPATH, value="//*[@id='u-1535117240']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]")
        like_button.click()
        sleep(1)

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(by=By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            sleep(3)
