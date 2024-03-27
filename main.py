import re
import sys
import time
from pathlib import Path
from typing import Type
from urllib.parse import urlparse

from dotenv import dotenv_values
from yt_dlp import YoutubeDL

from RVCMediaScraper import RVCMediaScraper
from CanvasEmbedRVC import CanvasEmbedRVC
from CanvasEmbedZoom import CanvasEmbedZoom
from ZoomScraper import ZoomScraper
from BaseScraper import BaseScraper
from selenium.webdriver.chrome.webdriver import WebDriver, Options

if __name__ != '__main__':
    print("ermm launch this script normally would you?")
    exit(1)

urls = []
file_name = sys.argv[1] or None
if file_name is None:
    print("Please provide a filename!")
    sys.exit(1)
file_name = Path(file_name)
file = open(file_name, "r")
for line in file:
    line = line.strip()
    if line:
        if line.startswith("#"):
            continue
        urls.append(line.strip())

driver_options = Options()
driver_options.add_argument("user-data-dir=selenium")
# driver_options.add_argument("headless")
driver = WebDriver(options=driver_options)

username = dotenv_values(".env")["username"]
password = dotenv_values(".env")["password"]

RVCScraper = RVCMediaScraper(driver, username, password)
RVCScraper.login()
for url in urls:
    if "rvcmedia.ust.hk" in url:
        print(RVCScraper.extract_media_url(url))


def zoomtest():
    zoom = ZoomScraper(driver, username, password)

    zoom.login()
    zoom.extract_media_url(
        "https://hkust.zoom.us/rec/play/zydOARToR_E3myKAFYEr5aD7naX9AC9AIHVIpBTrp0nBaDxtyPLzG1JHZTy7cILYQCxtiFRXhRWMQ0q7.baRBnEDxJMwFpyVL")

    zoom.quit()
