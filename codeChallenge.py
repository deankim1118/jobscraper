import requests
from bs4 import BeautifulSoup
import pandas as pd

class Scraper:
    def __init__(self, keywords = []):
        self.keywords = keywords
        self.job_lists = []
        self.df = pd.DataFrame()
        
    def get_response(self,keywords):
        response = requests.get(f"https://remoteok.com/remote-{keywords}-jobs", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
        
    def scraping_page(self, keywords):
        soup = self.get_response(keywords)
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
        self.df = pd.DataFrame(self.job_lists)
            
    def scraping_all(self):
        for u in self.keywords:
            self.scraping_page(u)  
        # print(self.df)
        
    def to_csv(self):
        excel_file = self.df.to_csv('jobs.csv')
        return excel_file
        
keywords = ["flutter","ios","java"]
              
scraping = Scraper(keywords)
scraping.scraping_all()
scraping.to_csv()