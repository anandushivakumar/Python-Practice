from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROM_UP = 150
PROM_DOWN = 10
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(5)

        self.go_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a")
        self.go_button.click()

        time.sleep(60)

        self.down_speed = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        self.up_speed = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        print(f"Test Completed! Download speed: {self.down_speed.text} & Upload speed: {self.up_speed.text}")

    def tweet(self):
        pass

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()