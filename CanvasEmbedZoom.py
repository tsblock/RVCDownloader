from BaseScraper import BaseScraper


class CanvasEmbedZoom(BaseScraper):
    def extract_media_url(self, url: str) -> str:
        super().extract_media_url(url)
        self.driver.get(url)

