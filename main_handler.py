import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from crawling import WebPage
from bs4 import BeautifulSoup
from lib import config , logger
from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_driver import DriverFunc

num_processes = 4
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")

def main():

    """
    1. Modulize
    2. Muti-processing
    3. OpenAi API 
    
    """
    # Driver setup
    driver = webdriver.Chrome(config.CHROME_EXE_LOCATION,options=options)

    # Create driver Func Object
    driverfunc = DriverFunc(driver)
    driverfunc.maximize_window()

    try:
        # To fb webpage
        driverfunc.to_url(config.LOGIN_URL)
        # logging to fb
        driverfunc.logging()
        # To target url
        driverfunc.to_url(config.TARGET_URL)

    except Exception as e:
        driver.close()
        raise Exception(e)

    # Set default height
    temp_height = 0

    # Go through all the way down
    # while True:
    for i in range(10):
        # Create driver func obj
        driverfunc = DriverFunc(driver)
        driverfunc.scroll_down()
        check_height = driverfunc.return_page_top_offset()

        if temp_height == check_height:
            break
        temp_height = check_height
    
    # Extract sublink
    sublink_soup = BeautifulSoup(driver.page_source, "html.parser")
    sublink = WebPage.crawl(sublink_soup)

    driver.close()
    results = WebPage.extract(sublink, num_processes)

    # Define dataframe , columns
    







if __name__ == '__main__':
    main()
