from selenium import webdriver
# To search elements
from selenium.webdriver.common.by import By
# To press buttons
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome()

driver.get(url=URL)

no_of_articles = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# no_of_articles.click()
all_portals = driver.find_element(by=By.LINK_TEXT, value="Community portal")
# all_portals.click()

search_bar = driver.find_element(by=By.NAME, value="search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
# print(no_of_articles.text)
while True:
    pass