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
            # # Send a GET request to the URL
            # response = requests.get(url)

            # # Raise an exception if the response is not successful
            # response.raise_for_status()

            # Parse the HTML content using BeautifulSoup




            titles = soup.find_all(
                "div", class_="x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r x126k92a")

            print(len(titles))



            # Create a list to store the extracted information
            extracted_info = []

            # Loop through each div and extract the relevant information
            # for div in divs:
            #     block = {
            #         'date': div.find('div', class_="date").text.strip(),
            #         'content': div.find('div', class_="content").text.strip()
            #     }
            #     extracted_info.append(block)

            # Write the extracted information to a CSV file in an ordered manner
            with open('extracted_info.csv', 'w', newline='') as csvfile:
                fieldnames = ['date', 'content']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for block in extracted_info:
                    writer.writerow(block)

            print('Web page crawled successfully and information extracted to CSV.')

        except Exception as e:
            # Log the error message with timestamp
            logger.error(f'{datetime.datetime.now()} - {str(e)}')


