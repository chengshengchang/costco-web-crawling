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

@dataclass
class DriverFunc:
    driver : object

    def logging(self):
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="login_form"]/div[2]/div[1]/label/input').send_keys(config.EMAIL)
            self.driver.find_element_by_xpath(
                '//*[@id="login_form"]/div[2]/div[2]/label/input').send_keys(config.PASSWORD)
            self.driver.find_element(By.XPATH,'//*[@id="login_form"]/div[2]/div[3]/div/div').click()
            time.sleep(3)
        except:
            logger.logger.error("Login error occur")

    def toTargetUrl(self,url):
        try:
            self.driver.get(url)
        except:
            logger.logger.error('URL is in valid')

    def maximizeWindow(self):
        self.driver.maximize_window()

    def scrollDown(self):
        self.driver.execute_script("window,scrollBy(0,1000)")
        logger.logger.info('Scrolling page down')
        time.sleep(2)

    def returnPageTopOffset(self):
        check_height = self.driver.execute_script(
            "return document.documentElement.ScrollTop || window,pageYOffset || documer")
        return check_height

    def expandPost(self):
        try:
            btn = self.driver.find_element(By.XPATH,"//div[text()='顯示更多']")
            btn.click()
        except:
            logger.logger.info("No post to expand")






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
    driverfunc.maximizeWindow()

    try:
        # To target url
        driverfunc.toTargetUrl(config.TARGET_URL)
        # 填入帳號密碼，並送出
        driverfunc.logging()


    except Exception as e:
        driver.close()
        raise Exception(e)

    temp_height = 0
    while True:
        driverfunc = DriverFunc(driver)
        driverfunc.scrollDown()
        driverfunc.expandPost()
        check_height = driverfunc.returnPageTopOffset()



        if temp_height == check_height:
            break
        temp_height = check_height
        print(temp_height)

    # driver.quit()



    soup = BeautifulSoup(driver.page_source, "html.parser")
    WebPage.crawl(root)


if __name__ == '__main__':
    main()
