import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from time import sleep
load_dotenv()

driver = webdriver.Chrome()
FORM_LINK = os.environ.get("FORM_LINK")
Listing_URL = os.environ.get("ZILLOW_URL")

# response = requests.get(url=Listing_URL).text
# soup = BeautifulSoup(response, 'html.parser')
# print(soup)
# property_list = soup.find_all(name="ul", class_="List-c11n-8-84-3__sc-1smrmqp-0")
# print(property_list)

driver.get(url=Listing_URL)
sleep(10)
property_list_div = driver.find_element(by=By.CSS_SELECTOR, value="#grid-search-results")
print(property_list_div)
property_list_div.click()
sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(10)
property_list = driver.find_elements(by=By.CLASS_NAME, value="ListItem-c11n-8-84-3__sc-10e22w8-0")
sleep(2)
# for i in range(10):
#     #In this case we're executing some Javascript, that's what the execute_script() method does.
#     #The method can accept the script as well as a HTML element.
#     #The modal in this case, becomes the arguments[0] in the script.
#     #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", property_list)
#     sleep(2)
# sleep(20)
property_links = driver.find_elements(by=By.CLASS_NAME, value="property-card-data")
for i in range(len(property_list)):
    item = property_list[i]
    item_info = item.text.split('\n')
    print(item_info)
    item_address = item_info[0]
    print(item_address)
    item_price = item_info[1]
    print(item_price)
    item_link = property_links[i]
    print(item_link)

    # driver.get(url=FORM_LINK)
    # fields = driver.find_elements(by=By.CLASS_NAME, value=".Xb9hP")
    # fields[0].send_keys(item_address)
    # fields[1].send_keys(item_price)
    # fields[2].send_keys(item_link)
    # sleep(2)
    # submit_button = driver.find_element(by=By.CLASS_NAME, value="NPEfkd")
    # submit_button.click()
    sleep(3)

# print(property_list)
