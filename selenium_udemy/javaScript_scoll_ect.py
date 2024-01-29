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
actual_list = []

### Variables 
url = "https://rahulshettyacademy.com/AutomationPractice/"
product = "bicycle"
##Chrome Driver
service_obj = Service("C:/Users/deank/OneDrive/Investments/Best_Reviews__Blog/Scraper/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj) 
driver.get(url)
driver.maximize_window()
### implicitly_wait(5) -> 5seconds is max time out...한번만 선언해 주면 된다! 모든 코드에 적용!
driver.implicitly_wait(5)
### JavaScript를 사용해서 Scroll 등 많은 것을 할 수 있다.
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
### Screen Shot 
#driver.get_screenshot_as_file("screen.png")
### Selenium Scroll Class 가 생겼다.
# iframe = driver.find_element(By.TAG_NAME, "iframe")
# scroll_origin = ScrollOrigin.from_element(iframe)
# webdriver.ActionChains(driver).scroll_from_origin(scroll_origin, 0, 700).perform()