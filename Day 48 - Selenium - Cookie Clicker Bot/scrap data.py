from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

driver = webdriver.Chrome()

driver.get(URL)
menu_items = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li")

# 1st Method

items = []
for item_ in menu_items:
    new_item = {}
    item = item_.text.split("\n")
    new_item["date"] = item[0]
    new_item["event"] = item[1]

    items.append(new_item)

all_events = {i:items[i] for i in range(len(items))}
print(all_events)

# 2nd Method

events_list = {}
for i in range(len(menu_items)):
    events_list[i] = {
        "date": menu_items[i].text.split("\n")[0],
        "event": menu_items[i].text.split("\n")[1],
    }
print(events_list)
while True:
    pass
