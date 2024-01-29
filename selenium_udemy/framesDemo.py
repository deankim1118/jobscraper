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
url = "https://the-internet.herokuapp.com/iframe"
product = "bicycle"
##Chrome Driver
service_obj = Service("C:/Users/deank/OneDrive/Investments/Best_Reviews__Blog/Scraper/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj) 
driver.get(url)
driver.maximize_window()
### implicitly_wait(5) -> 5seconds is max time out...한번만 선언해 주면 된다! 모든 코드에 적용!
driver.implicitly_wait(5)
### Handle iframe another HTML inside of HTML
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Switch to frame is completed")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)