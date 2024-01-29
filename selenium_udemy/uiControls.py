from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

### Keeping browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

### Variables 
url = "https://shopping.google.com/"
product = "bicycle"
##Chrome Driver
service_obj = Service("C:/Users/deank/OneDrive/Investments/Best_Reviews__Blog/Scraper/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj) 
driver.get(url)
driver.maximize_window()

### Search Products on Google Shopping
## Enter product
driver.find_element(By.NAME, "q").send_keys(product)
driver.find_element(By.XPATH, "//*[@id='kO001e']/div/div/c-wiz/form/div[2]/div[1]/button/div").click()
time.sleep(3)

### Click rating 4 and up
rating_4 = driver.find_elements(By.CLASS_NAME, 'cNaB2e')[0]
# Error 처리 False 면 Error
assert "4" in rating_4.text
rating_4.click()

