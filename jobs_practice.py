from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

## with as는 반드시 close()를 사용해야되는데 까먹고 안 닫는 경우를 위해 만들어졌다. p = sync_playwright().start() Initialize 한거랑 같은 뜻
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")
    # time.sleep(5)
    # page.click("button.Aside_searchButton__Xhqq3")
    # time.sleep(5)
    # page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
    # time.sleep(5)
    # page.keyboard.down("Enter")
    # time.sleep(7)
    # page.click("a#search_tab_position")
    for x in range(5):
        time.sleep(3)
        page.keyboard.down("End")
    content = page.content()
    p.stop()
    
## BeautifulSoup
jobs_db = []
soup = BeautifulSoup(content, "html.parser")
jobs = soup.find_all("div", class_="JobCard_container__FqChn")
for job in jobs: 
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__ddkwM").text
    company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
    location = job.find("span", class_="JobCard_location__2EOr5").text
    reward = job.find("span", class_="JobCard_reward__sdyHn").text
    
    job = {
        "title": title,
        "company_name": company_name,
        "location": location,
        "reward": reward,
        "link": link,
    }
    jobs_db.append(job)

with open("jobs.csv", mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title","Company","Location","Reward","Link",])
    
    for job in jobs_db:
        ### .values or .keys 메소드는 Dictionarie의 Value or key를 가져와서 List로 만들어준다.
        writer.writerow(job.values())
    file.close()