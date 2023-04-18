import pandas as pd
import time
from pandas.core.frame import DataFrame
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from crawling import WebPage
import csv
import requests
from bs4 import BeautifulSoup
import logging
import datetime
from lib import config , logger
from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from fake_useragent import UserAgent


@dataclass
class DriverFunc:
    driver : object

    def logging(self):
        try:
            # time.sleep(1)
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
            elem = self.driver.find_element_by_id("email")
            elem.send_keys(config.EMAIL)

            elem = self.driver.find_element_by_id("pass")
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

def main():


    # Chrome block avoid
    options = webdriver.ChromeOptions()
    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
    }
    options.add_experimental_option('prefs', prefs)
    options.add_argument("disable-infobars")

    # Driver setup
    driver = webdriver.Chrome(config.CHROME_EXE_LOCATION,options=options)

    # Create driver Func Object
    driverfunc = DriverFunc(driver)
    driverfunc.maximize_window()

    try:
        driverfunc.to_url(config.LOGIN_URL)
        driverfunc.logging()
        # To target url
        driverfunc.to_url(config.TARGET_URL)
        time.sleep(2)


    except Exception as e:
        driver.close()
        raise Exception(e)

    temp_height = 0
    # while True:
    for i in range(10):
        driverfunc = DriverFunc(driver)
        driverfunc.scroll_down()
        # driverfunc.expand_post()

        check_height = driverfunc.return_page_top_offset()

        if temp_height == check_height:
            break
        temp_height = check_height


    soup = BeautifulSoup(driver.page_source, "html.parser")
    WebPage.crawl(soup)


if __name__ == '__main__':
    main()
