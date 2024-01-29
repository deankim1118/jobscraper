from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

## Keeping browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#driver = webdriver.Chrome(options=options)

url = "https://shopping.google.com/"
service_obj = Service("C:/Users/deank/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe") # seleniumManager #
driver = webdriver.Chrome(options=options, service=service_obj) 
driver.get(url)
driver.maximize_window()

## ID, Xpath, CSSSelector, ClassName, name, LinkText
# ClassName 
driver.find_element(By.NAME, "q").send_keys("bicycle")
# driver.implicitly_wait(5)
# # Xpath
# driver.find_element(By.XPATH, "//*[@id='kO001e']/div/div/c-wiz/form/div[2]/div[1]/button/div").click()
# driver.implicitly_wait(5)
# # CSSSelector .classname #ID
# # driver.find_element(By.CSS_SELECTOR, "input[name='q']").clear()
# # driver.find_element(By.CSS_SELECTOR, "input[name='q']").send_keys("bicycle helmet")
# # driver.implicitly_wait(5)
# # # Index Xpath 
# # driver.find_element(By.XPATH,"(//span[@class='_-n5'])[1]").click()
# # LinkText
# driver.find_element(By.PARTIAL_LINK_TEXT, "OUXI").click()
# 아무것도 없을 때 Text로 Locate 할 수 있다.
#ex) -> # driver.find_element(By.XPATH, "//button[text()='Save New Password']")
time.sleep(2)

suggestions = driver.find_elements(By.CSS_SELECTOR, "li[class='zEqjYe']")

for s in suggestions:
    if s.text == "bicycle seat":
        s.click()
        break
# Error 처리 False 가 되면 Error 가 난다.   
assert driver.find_element(By.NAME, "q").get_attribute("value") == "bicycle seat"