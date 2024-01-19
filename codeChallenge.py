import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, keywords = []):
        self.keywords = keywords
 
        
    def scraping_page(self):
        for key in self.keywords:
            response = requests.get(f"https://remoteok.com/remote-{key}-jobs", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
            soup = BeautifulSoup(response.content, "html.parser")
            print(response.status_code)


scraping = Scraper(["flutter", "ios"])
scraping.scraping_page()