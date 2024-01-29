from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

## Keeping browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#driver = webdriver.Chrome(options=options)

url = "https://rahulshettyacademy.com/loginpagePractise/"
service_obj = Service("C:/Users/deank/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe") # seleniumManager #
driver = webdriver.Chrome(options=options, service=service_obj) 
driver.get(url)
driver.maximize_window()

dropdown = Select(driver.find_element(By.XPATH, "//*[@id='login-form']/div[5]/select"))
# dropdown.select_by_index(1)
# dropdown.select_by_value("consult")
dropdown.select_by_visible_text("Teacher")