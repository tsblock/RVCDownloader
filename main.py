import sys
import time

from dotenv import dotenv_values
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from yt_dlp import YoutubeDL

urls = []
file_name = sys.argv[1] or None
if file_name is None:
    print("Please provide a filename!")
    sys.exit(1)
file = open(file_name, "r")
for line in file:
    urls.append(line.strip())

driver_options = Options()
driver_options.add_argument("user-data-dir=selenium")
# driver_options.add_argument("headless")
driver = webdriver.Chrome(options=driver_options)
driver.get(urls[0])


def handle_microsoft_login(driver: webdriver.Chrome):
    try:
        driver.find_element(By.XPATH, "//*[@id=\"tilesHolder\"]/div[1]/div/div[1]/div/div[2]/div").click()
    except NoSuchElementException:
        driver.implicitly_wait(1.0)
        driver.find_element(By.XPATH, "//*[@id=\"i0116\"]").send_keys(dotenv_values(".env")["MAIL"])
        driver.implicitly_wait(1.0)
        driver.find_element(By.XPATH, "//*[@id=\"idSIButton9\"]").click()
    finally:
        time.sleep(1.0)
        driver.implicitly_wait(2.0)
        driver.find_element(By.XPATH, "//*[@id=\"i0118\"]").send_keys(dotenv_values(".env")["PASSWORD"])
        driver.implicitly_wait(1.0)
        driver.find_element(By.XPATH, "//*[@id=\"idSIButton9\"]").click()
    WebDriverWait(driver, timeout=30.0).until(lambda x: "microsoftonline" not in driver.current_url)
    WebDriverWait(driver, timeout=60.0).until(lambda x: "duosecurity" not in driver.current_url)


def handle_zoom(driver: webdriver.Chrome):
    if not "zoom.us/signin" in driver.current_url:
        return
    driver.implicitly_wait(1.0)
    driver.find_element(By.CLASS_NAME, "zm-login-methods__item").click()
    handle_microsoft_login(driver)


def find_rvc_m3u8_url(driver: webdriver.Chrome, url: str) -> str:
    driver.get(url)
    driver.implicitly_wait(1.0)
    driver.find_element(By.ID, "rvcMediaPlayer")
    media_url = driver.execute_script(
        'return jwplayer("rvcMediaPlayer").getConfig()["playlist"][0]["sources"][0]["file"]')
    return media_url


#TODO: make yt-dlp download video
def download_url(url: str):
    ytdlp_options = {}
    ytdl = YoutubeDL()
    pass


if "microsoftonline" in driver.current_url:
    handle_microsoft_login(driver)


for url in urls:

    actual_url = find_rvc_m3u8_url(driver, url)
    download_url(actual_url)
