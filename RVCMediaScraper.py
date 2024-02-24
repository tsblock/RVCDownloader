from selenium.webdriver.common.by import By

from BaseScraper import BaseScraper


class RVCMediaScraper(BaseScraper):
    def extract_media_url(self, url: str) -> str:
        super().extract_media_url(url)
        self.driver.get(url)
        self.wait_until_element(1.0, By.ID, "rvcMediaPlayer")

        # Credit to evnchn for js code that finds m3u8 url in rvcmedia
        # https://github.com/evnchn/RVC-SB/blob/master/rvc-sb.py#L3
        media_url = self.driver.execute_script(
            'return jwplayer("rvcMediaPlayer").getConfig()["playlist"][0]["sources"][0]["file"]'
        )
        return media_url
