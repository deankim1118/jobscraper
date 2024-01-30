from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

### Keeping browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
## Ignore certificate errors
options.add_argument("--ignore-certificate-errors")
browserSortedVeggies = []

### Variables 
url = "https://rahulshettyacademy.com/angularpractice"
product = "bicycle"
##Chrome Driver
service_obj = Service("C:/Users/deank/OneDrive/Investments/Best_Reviews__Blog/Scraper/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj) 
driver.get(url)
# driver.maximize_window()
### implicitly_wait(5) -> 5seconds is max time out...한번만 선언해 주면 된다! 모든 코드에 적용!
driver.implicitly_wait(5)

### //a[contains(@href, "shop")]  ,  //a[href*="shop"]  CSS Selector
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
        
driver.find_element(By.XPATH, "//a[contains(@class, 'btn-primary')]").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("united")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United States of America")))
driver.find_element(By.LINK_TEXT, "United States of America").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()