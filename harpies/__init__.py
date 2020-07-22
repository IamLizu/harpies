import sys
import os
import uraiko
from bs4 import BeautifulSoup
import requests
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

log_file = os.path.join(os.path.normpath(os.path.expanduser('~/Documents/')), 'harpies.log')

file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def preview_data(link):
    logger.info("Checking " + link)
    uLink = uraiko.url_check(link)
    logger.info("Downloading the html page")

    response = requests.get(uLink)
    logger.info("Parsing the html page")
    soup = BeautifulSoup(response.text, "html.parser")

    logger.info("Saving meta datas into variables")
    metaTitle = soup.find("meta", property="og:title")["content"]
    metaDes = soup.find("meta", property="og:description")["content"]
    metaImg = soup.find("meta", property="og:image")["content"]
    metaUrl = soup.find("meta", property="og:url")["content"]

    logger.info("creating json object with data")
    metas = {
        "title": metaTitle,
        "description": metaDes,
        "image": metaImg,
        "url": metaUrl
        }
    
    metaJson = json.dumps(metas)

    return metaJson