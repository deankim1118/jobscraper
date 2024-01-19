import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        self.job_lists = []
        
    def get_response(self,url):
        response = requests.get(f"https://remoteok.com/remote-{url}-jobs", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
        
    def scraping_page(self, url):
        soup = self.get_response(url)
        jobs = soup.find("table", id="jobsboard").find_all("td", class_="company_and_position")[1:]

        for job in jobs:
            company = job.find("h3")
            title = job.find("h2")
            if len(job.find_all("div", class_="location")) >= 2:
                location, *others, income = job.find_all("div", class_="location")
            else: 
                location = job.find("div", class_="location")
            
            job_data = {
                "company": company.text.strip(),
                "title": title.text.strip(),
                "location": location.text,
                "income": income.text
            }
            self.job_lists.append(job_data)
            
    def scraping_all(self, url = []):
        for u in url:
            self.scraping_page(u)  
        print(self.job_lists)
              
scraping = Scraper()
scraping.scraping_all(["flutter","ios","java"])