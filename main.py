import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
    print(f"Scraping is working on {url}...")
    response = requests.get(url)

    soup = BeautifulSoup(response.content,"html.parser")

#class는 파이썬 명령어 이기 때문에 _를 꼭 붙여줘야된다.
    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

    for job in jobs:
        title = job.find("span", class_="title").text
        company, position, region = job.find_all("span", class_="company")
        company = company
        region = region
        position = position
        url = job.find("div", class_="tooltip").next_sibling["href"]
    
        job_date = {
        "title": title,
        "company": company.text,
        "region": region.text,
        "position": position.text,
        "url": f"https://weworkremotely.com{url}",
    }
        all_jobs.append(job_date)
        

def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")

    buttons = len(soup.find("div", class_="pagination").find_all("span", class_="page"))
    return buttons

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for page in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={page+1}"
    scrape_page(url)

print(len(all_jobs))
