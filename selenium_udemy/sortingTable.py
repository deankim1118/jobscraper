import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

### Keeping browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
## Ignore certificate errors
options.add_argument("--ignore-certificate-errors")
browserSortedVeggies = []

### Variables 
url = "https://rahulshettyacademy.com/seleniumPractise/#/offers"
product = "bicycle"
##Chrome Driver
service_obj = Service("C:/Users/deank/OneDrive/Investments/Best_Reviews__Blog/Scraper/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj) 
driver.get(url)
# driver.maximize_window()
### implicitly_wait(5) -> 5seconds is max time out...한번만 선언해 주면 된다! 모든 코드에 적용!
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in veggieWebElements:
    browserSortedVeggies.append(element.text)
    
orginalBrowserSortedVeggies = browserSortedVeggies.copy()
browserSortedVeggies.sort()

assert orginalBrowserSortedVeggies == browserSortedVeggies