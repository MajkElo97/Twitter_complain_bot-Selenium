from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "your email here"
TWITTER_PASSWORD = "your password here"
CHROME_DRIVER_PATH = 'C:\Development\chromedriver.exe'
URL_SPEEDTEST = "https://www.speedtest.net/"
URL_TWITTER = "https://twitter.com/i/flow/login"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url=URL_SPEEDTEST)
        self.driver.maximize_window()
        sleep(2)
        accept_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        accept_button.click()
        sleep(2)
        start_button = self.driver.find_element(by=By.XPATH,
                                                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_button.click()
        sleep(90)
        self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, 'upload-speed').text
        print(f"Download: {self.down}")
        print(f"Upload: {self.up}")
        # self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get(url=URL_TWITTER)
        self.driver.maximize_window()
        sleep(2)

        email = self.driver.find_element(by=By.NAME, value="text")
        email.send_keys(TWITTER_EMAIL)
        accept_button = self.driver.find_element(by=By.XPATH,
                                                 value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        accept_button.click()
        sleep(2)

        passw = self.driver.find_element(by=By.NAME, value="password")
        passw.send_keys(TWITTER_PASSWORD)
        accept_button = self.driver.find_element(by=By.XPATH,
                                                 value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        accept_button.click()
        sleep(5)
        accept_button = self.driver.find_element(by=By.XPATH,
                                                 value='//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]')
        accept_button.click()
        sleep(5)

        msg = f"Hey internet provider, why is my speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        print(msg)
        input_field = self.driver.find_element(by=By.CLASS_NAME,
                                               value='public-DraftEditor-content')
        input_field.send_keys(msg)
        sleep(2)
        accept_button = self.driver.find_element(by=By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        accept_button.click()
        sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

