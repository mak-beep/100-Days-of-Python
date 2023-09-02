from selenium import webdriver
# To search elements
from selenium.webdriver.common.by import By
# for keeping track of time
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"
GAME_MINUTES = 1
START_TIME = int(time.monotonic())
i = 0
check_time = 0

driver = webdriver.Chrome()

driver.get(url=URL)

cookie = driver.find_element(by=By.ID, value="cookie")

while True:
    cookie.click()
    all_items = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
    items = [item.text for item in all_items]
    money = driver.find_element(by=By.ID, value="money")
    current_time = int(time.monotonic())
    if current_time - START_TIME >= (GAME_MINUTES*60):
        speed = driver.find_element(by=By.ID, value="cps")
        print(speed.text)
        exit()
    if current_time - check_time >= 5:
        for i in range(len(total_options)-2, -1, -1):
            item = total_options[i]
            point = item.text.split("-")[1].strip().replace(",","")
            if float(money.text) >= float(point):
                # print(item.text)
                # print(f"{item.text} is Selected.")
                item.click()
                break

            check_time = int(time.monotonic())


