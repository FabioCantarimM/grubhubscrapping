from crawlers.GrubHub import GrubHubCrawler
from entity.Restaurant import Restaurant

class GeneralCrawler:

    def __init__(self):
        pass

    def find_crawler(self, name: str, url: str) -> Restaurant:
        do = f"crawler_{name}"
        if hasattr(self, do) and callable(func := getattr(self, do)):
            return func(url)

    def crawler_GrubHub(self, url):
        return GrubHubCrawler(url).execute()