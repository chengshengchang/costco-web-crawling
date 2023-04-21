import csv
import requests
from bs4 import BeautifulSoup
import logging
import datetime
from content_extracter import GPT3Model
from multiprocessing import Pool
import csv
from web_driver import DriverFunc
from selenium import webdriver
from lib import config , logger


options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")

# Set up a basic configuration for the logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


class WebPage:

    @staticmethod
    def crawl(soup):
        try:
            sublink = soup.find_all(
                "a", class_="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa xo1l8bm")

            # Extract href attribute values and store them in a list
            href_list = []
            for anchor_tag in sublink:
                href = anchor_tag['href']
                href_list.append(href)

            return href_list


        except Exception as e:
            # Log the error message with timestamp
            logger.error(f'{datetime.datetime.now()} - {str(e)}')

    @staticmethod
    def scrape_url(url):
        driver = webdriver.Chrome(config.CHROME_EXE_LOCATION,options=options)
        driverfunc = DriverFunc(driver)
        driverfunc.maximize_window()

        driverfunc.to_url(url)
        driverfunc.logging_sublink()

        # 之後要加 讓他不要跑 chrome 介面出來
        

        model = GPT3Model("text-davinci-003")
        title_prompt = "Write a paragraph about the benefits of meditation."
        generated_text = model.generate_text(title_prompt)

        # Print the generated text
        print(generated_text)

    @staticmethod
    def extract(urls, num_processes):
        try:
            with Pool(num_processes) as p:
                results = p.map(WebPage.scrape_url,urls)
            return results

            


        except Exception as e:
            # Log the error message with timestamp
            logger.error(f'{datetime.datetime.now()} - {str(e)}')


