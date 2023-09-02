from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import os
from dotenv import load_dotenv
from time import sleep
load_dotenv()

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3689679460&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"

driver = webdriver.Chrome()

driver.get(url=URL)

sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")

sign_in_button.click()

sleep(5)
username_field = driver.find_element(by=By.ID, value="username")
username_field.send_keys(EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)
# sleep(10)
sleep(5)
jobs_listings = driver.find_elements(by=By.CLASS_NAME, value="job-card-container--clickable")
print(jobs_listings)
for listing in jobs_listings:
    # print(listing.text)
    listing.click()
    sleep(2)
    # For Applying to Jobs
    try:
        apply_button = driver.find_element(by=By.CLASS_NAME, value="jobs-s-apply")
        # print(apply_button)
        apply_button.click()
        sleep(2)
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("aria-label") == "Continue to next step":
            print("Multi-Step Application. So closing to skip.")
            close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()
            sleep(2)
            discard_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")
            discard_button.click()
            sleep(2)
        else:
            submit_button.click()
    except NoSuchElementException:
        print("No Apply Button. Skipped.")

    # For Saving Jobs

    # save_button = driver.find_element(by=By.CLASS_NAME, value="jobs-save-button")
    # save_button.click()

while True:
    pass
