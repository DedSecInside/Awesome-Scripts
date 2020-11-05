# Create your tasks here
from __future__ import absolute_import, unicode_literals
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta
from.models import Wallpaper
from pyfcm import FCMNotification
import os.path
from .utils import *
push_service = FCMNotification(api_key="")

PHANTOMJS_PATH = ''
if(not os.path.exists(PHANTOMJS_PATH)):
    PHANTOMJS_PATH = '../phantomjs'

max_records = 5000
most_wanted_players = []

def get_latest_wallpapers():
    """
    Downloads a browser.

    Args:
    """
    browser = webdriver.PhantomJS(PHANTOMJS_PATH, service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
    today_date = time.strftime("%d+%b+%Y")  
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_date = yesterday.strftime('%d+%b+%Y')
    first_page_url = 'http://www.espncricinfo.com/ci/content/image/?datefrom='+yesterday_date+'&dateupto='+today_date+';'
    browser.get(first_page_url)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "img-wrap")))
    time.sleep(2)
    # let's parse our html
    soup = BeautifulSoup(browser.page_source, "html.parser")
    images = soup.find_all('div', class_='picture')
    for image in images:
        url = "http://www.espncricinfo.com/" + image.find('a').get('href')
        print(url)