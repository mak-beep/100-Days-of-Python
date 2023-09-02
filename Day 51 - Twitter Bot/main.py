import os
from time import sleep
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


from dotenv import load_dotenv

load_dotenv()

USERNAME = os.environ.get("USER")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

PROMISED_DOWN_SPEED = 150
PROMISED_UP_SPEED = 10
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://www.twitter.com/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down_speed = 80.7
        self.up_speed = 5.3

    def get_internet_speed(self):
        self.driver.get(url=SPEED_TEST_URL)
        # sleep(5)
        go_button = self.driver.find_element(by=By.XPATH,
                                             value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        print(go_button)
        go_button.click()
        sleep(40)
        self.down_speed = self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text
        self.up_speed = self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text
        print(f"Download Speed = {self.down_speed}")
        print(f"Upload Speed = {self.up_speed}")

    def tweet_at_provider(self):
        self.driver.get(url=TWITTER_URL)
        sleep(10)
        sign_in_button = self.driver.find_element(by=By.XPATH,
                                                  value="//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div")
        print(sign_in_button)
        sign_in_button.click()
        sleep(15)

        email_field = self.driver.find_element(by=By.NAME, value="text")
        email_field.send_keys(EMAIL)
        sleep(2)
        next_button = self.driver.find_element(by=By.XPATH,
                                               value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span")
        print(next_button)
        next_button.click()

        sleep(10)
        try:
            user_field = self.driver.find_element(by=By.NAME, value="text")
            user_field.send_keys(USERNAME)
            sleep(2)
            next_button = self.driver.find_element(by=By.XPATH,
                                                   value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div")
            print(next_button)
            next_button.click()
            sleep(10)
        except NoSuchElementException:
            pass
        password_field = self.driver.find_element(by=By.NAME, value="password")
        password_field.send_keys(PASSWORD)
        sleep(2)
        log_in_button = self.driver.find_element(by=By.XPATH,
                                                 value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
        print(log_in_button)
        log_in_button.click()
        sleep(30)

        tweet_compose = self.driver.find_element(by=By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]')
        tweet_compose.click()

        tweet = (f"Hey Internet Provider, why is my internet speed {self.down_speed}down/{self.up_speed}up when I pay "
                 f"for {PROMISED_DOWN_SPEED}down/{PROMISED_UP_SPEED}up?")
        tweet_compose.send_keys(tweet)
        sleep(3)
        sleep(10)
        post_button = self.driver.find_element(by=By.XPATH,
                                               value="//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span")
        post_button.click()

        sleep(5)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
