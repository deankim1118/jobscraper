import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

### Keeping browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
actual_list = []

### Variables 
url = "https://rahulshettyacademy.com/seleniumPractise/#/"
product = "bicycle"
##Chrome Driver
service_obj = Service("C:/Users/deank/OneDrive/Investments/Best_Reviews__Blog/Scraper/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj) 
driver.get(url)
driver.maximize_window()
### implicitly_wait(5) -> 5seconds is max time out...한번만 선언해 주면 된다! 모든 코드에 적용!
driver.implicitly_wait(5)
### Implicitly wait은 List가 0개든 100개든 일단 만들어지면 기다리지않고 다음 코드로 넘어가버린다. 그래서 time.sleep()이든 explicit Wait을 써줘야된다.
wait = WebDriverWait(driver, 10)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") #List
count = len(results)
assert count > 0
for result in results:
    actual_list.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()
    
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# Sum prices
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p") 
sum = 0
for price in prices:
    sum += int(price.text)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount
# input Promocode
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
### Explicit Wait -> wait(driver, 10) -> Max 10초 까지 기다린다 not globally -> .until(expected_conditions)을 써줘서 조건을 설정한다.
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".promoInfo")))
assert driver.find_element(By.CSS_SELECTOR,".promoInfo").text  ==  "Code applied ..!"

