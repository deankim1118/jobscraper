import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


### Keeping browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
actual_list = []

### Variables 
url = "https://the-internet.herokuapp.com/windows"
##Chrome Driver
service_obj = Service("C:/Users/deank/OneDrive/Investments/Best_Reviews__Blog/Scraper/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj) 
driver.get(url)
driver.maximize_window()
### implicitly_wait(5) -> 5seconds is max time out...한번만 선언해 주면 된다! 모든 코드에 적용!
driver.implicitly_wait(5)
### Implicitly wait은 List가 0개든 100개든 일단 만들어지면 기다리지않고 다음 코드로 넘어가버린다. 그래서 time.sleep()이든 explicit Wait을 써줘야된다.


# Open a new window
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowOpened = driver.window_handles
driver.switch_to.window(windowOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windowOpened[0])
print(driver.find_element(By.TAG_NAME, "h3").text)