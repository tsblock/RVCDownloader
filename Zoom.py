from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from BaseScraper import BaseScraper


class ZoomScraper(BaseScraper):
    def check_session_alive(self) -> bool:
        self.driver.get("https://hkust.zoom.us/signin")
        try:
            WebDriverWait(self.driver, timeout=3.0).until(
                lambda _: self.driver.current_url == "https://hkust.zoom.us/profile")
        except TimeoutException:
            return False
        return True

    def extract_media_url(self, url: str) -> str:
        super().extract_media_url(url)
        self.driver.get(url)
