import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from lib import config , logger
from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Pool
import csv

@dataclass
class DriverFunc:
    driver : object
    

    def logging_sublink(self):
        # try:
            self.driver.find_element_by_xpath(
                '//*[@id="login_form"]/div[2]/div[1]/label/input').send_keys(config.EMAIL)
            self.driver.find_element_by_xpath(
                '//*[@id="login_form"]/div[2]/div[2]/label/input').send_keys(config.PASSWORD)
            self.driver.find_element(By.XPATH,'//*[@id="login_form"]/div[2]/div[3]/div/div').click()
            time.sleep(3)
        # except:
        #     logger.logger.error("Login error occur")
    def logging(self):
        try:
            # time.sleep(1)
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//input[@id="email"]')))
            elem = self.driver.find_element(By.XPATH,'//input[@id="email"]')
            elem.send_keys(config.EMAIL)

            elem = self.driver.find_element(By.XPATH,'//input[@id="pass"]')
            elem.send_keys(config.PASSWORD)

            elem.send_keys(Keys.RETURN)
            time.sleep(5)
        except:
            logger.logger.error("Login error occur")

    def to_url(self,url):
        try:
            self.driver.get(url)
            time.sleep(1)
        except:
            logger.logger.error('URL is in valid')

    def maximize_window(self):
        self.driver.maximize_window()

    def scroll_down(self):
        self.driver.execute_script("window,scrollBy(0,1000)")
        logger.logger.info('Scrolling page down')
        time.sleep(1)

    def return_page_top_offset(self):
        check_height = self.driver.execute_script(
            "return document.documentElement.ScrollTop || window,pageYOffset || documer")
        return check_height

    def expand_post(self):
        try:
            btn = self.driver.find_element(By.XPATH,"//div[text()='顯示更多']")
            btn.click()
        except:
            logger.logger.info("No post to expand")

    def expand_comment(self):
        # #查看更多留言
        # # try:
        # btn = self.driver.find_element(
        #     By.XPATH, '//div[@class="x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv"]')
        # btn.click()
        # # except:
        #     # logger.logger.info("No comment to expand")

        # temp_height = 0
        # while True:
        #     ctn = self.driver.find_element(
        #         By.XPATH, '//div[@class="x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv"]')
        pass