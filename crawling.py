import csv
import requests
from bs4 import BeautifulSoup
import logging
import datetime


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
            titles = soup.find_all(
                "a", class_="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa xo1l8bm")

            # Extract href attribute values and store them in a list
            href_list = []
            for anchor_tag in titles:
                href = anchor_tag['href']
                href_list.append(href)

            return href_list


        except Exception as e:
            # Log the error message with timestamp
            logger.error(f'{datetime.datetime.now()} - {str(e)}')

    @staticmethod
    def extract(link):
        try:
            pass
        except Exception as e:
            # Log the error message with timestamp
            logger.error(f'{datetime.datetime.now()} - {str(e)}')


