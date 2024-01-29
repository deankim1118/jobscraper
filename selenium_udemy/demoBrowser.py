from selenium import webdriver
from selenium.webdriver.chrome.service import Service

## Keeping browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#driver = webdriver.Chrome(options=options)
 
#service_obj = Service() #seleniumManager #크롬드라이버를 다운로드하고 실행하기 때문에 느릴 수 있다. Google driver를 설치할 필요없다.
service_obj = Service("C:/Users/deank/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe") # seleniumManager #
driver = webdriver.Chrome(options=options, service=service_obj) 
driver.maximize_window()
driver.get("https://google.com/")
driver.get("https://www.google.com/search?tbm=shop&hl=en&psb=1&q=bycicle")
# driver.minimize_window()
driver.refresh()
driver.back()
# driver.forward()
driver.close()
# print(driver.title) # Title of tab
# print(driver.current_url)  # Current URL 
