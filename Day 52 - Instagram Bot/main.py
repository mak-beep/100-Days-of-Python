import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
SIMILAR_ACCOUNT = os.environ.get("SIMILAR_ACCOUNT")

URL = "https://www.instagram.com/"


class InstaFollower:
    def __init__(self):
        self.followers_list = None
        self.driver = webdriver.Chrome()

    def login(self):
        print("login")
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        sleep(10)
        username_field = self.driver.find_element(by=By.NAME, value="username")
        username_field.send_keys(USER)
        password_field = self.driver.find_element(by=By.NAME, value="password")
        password_field.send_keys(PASSWORD)
        login_button = self.driver.find_element(by=By.XPATH, value="//*[@id='loginForm']/div/div[3]/button")
        login_button.click()
        sleep(10)

    def get_followers(self):
        self.driver.get(url=URL + SIMILAR_ACCOUNT)
        sleep(20)
        followers_link = self.driver.find_element(by=By.CSS_SELECTOR, value='ul li a')
        print(followers_link)
        sleep(5)
        followers_link.click()
        sleep(5)
        # self.followers_list = self.driver.find_elements(by=By.XPATH,
        #                                                 value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button')
        # print(self.followers_list)
        self.followers_list = self.driver.find_elements(by=By.CSS_SELECTOR, value='._aano button')
        print(self.followers_list)


    def follow(self):
        for follower in self.followers_list:
            try:
                follower.click()
                sleep(5)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()



bot = InstaFollower()

bot.login()
bot.get_followers()
bot.follow()

while True:
    pass
