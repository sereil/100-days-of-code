from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\\Dev\\chromedriver.exe"
COOKIE_CLICKER = "https://orteil.dashnet.org/cookieclicker/"

def launchBrowser():
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(COOKIE_CLICKER)
    
    time.sleep(5)
    
    language_EN = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
    language_EN.click()
    
    time.sleep(3)
    cookie_btn = driver.find_element(By.CSS_SELECTOR, "#bigCookie")
    
    for n in range(1000):
        cookie_btn.click()
    
    while True:
        pass

launchBrowser()    
    