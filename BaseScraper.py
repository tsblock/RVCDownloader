import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseScraper:
    def __init__(self, driver: webdriver.Chrome, username: str, password: str):
        self.driver = driver
        self.username = username
        self.password = password
        self.bootstrap_url = "https://cas.ust.hk/cas/login?service=https://hkust.edu.hk/stu_intranet/"

    def wait_until_element(self, timeout: float, by: str, value: str) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))

    def login(self):
        # Bootstrap authentication, get us to Microsoft SSO page
        self.driver.get(self.bootstrap_url)
        # Sometimes SSO would redirect to "Select your HKUST affiliation" page instead of Microsoft SSO
        if "https://shib.ust.hk/idp/discovery.jsp" in self.driver.current_url:
            # Select "Remember this selection permanently" for good measure
            self.driver.find_element(By.ID, "rememberme").click()
            self.driver.find_element(By.XPATH,
                                     '//*[@id="https://sts.windows.net/c917f3e2-9322-4926-9bb3-daca730413ca/"]').click()
        try:
            # If we have already logged in before, the login page would show account selector
            # This automatically clicks the first account in the selector
            self.wait_until_element(1.0, By.XPATH,
                                    '//*[@id="tilesHolder"]/div[1]/div/div[1]/div/div[2]/div').click()
        except TimeoutException:
            # Username input
            # Only happens when logging in for the first time
            self.wait_until_element(2.0, By.ID, "i0116").send_keys(self.username)
            self.wait_until_element(2.0, By.ID, 'idSIButton9').click()
        finally:
            # Password input
            self.wait_until_element(2.0, By.ID, "i0118").send_keys(self.password)
            self.wait_until_element(2.0, By.ID, 'idSIButton9').click()

        WebDriverWait(self.driver, timeout=3.0).until(
            lambda _: "microsoftonline" not in self.driver.current_url
        )

        # Let user themselves do 2FA
        WebDriverWait(self.driver, timeout=60.0).until(
            lambda _: "duosecurity" not in self.driver.current_url
        )

    def check_session_alive(self) -> bool:
        # To check if our session expire, we can just visit a site requires authentication
        # And see if we are stuck in an SSO page
        self.driver.get(self.bootstrap_url)
        try:
            WebDriverWait(self.driver, 3.0).until(
                lambda _: "https://hkust.edu.hk/stu_intranet" in self.driver.current_url)
        except TimeoutError:
            return False
        return True

    def extract_media_url(self, url: str) -> str:
        if not self.check_session_alive():
            self.login()

    def quit(self):
        self.driver.quit()