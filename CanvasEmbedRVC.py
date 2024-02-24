from selenium.webdriver.common.by import By

from BaseScraper import BaseScraper
from RVCMediaScraper import RVCMediaScraper


class CanvasEmbedRVC(BaseScraper):
    # Since this is just a iframe with RVCMedia embedded in a Canvas page
    # We can just get the url and let RVCMediaScraper handle the rest
    def extract_media_url(self, url: str):
        self.driver.get(url)
        iframe_rvc_url = self.wait_until_element(3.0, By.CSS_SELECTOR, ".show-content > div:nth-child(2) > iframe:nth-child(1)").get_attribute("src")
        rvc_scraper = RVCMediaScraper(self.driver, self.username, self.password)
        return rvc_scraper.extract_media_url(iframe_rvc_url)
        pass
