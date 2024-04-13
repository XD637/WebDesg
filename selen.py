from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service=Service(executable_path="chromedriver.exe")

# Initialize the Chrome driver with options
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:8000/")

time.sleep(20)

driver.quit()