from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

LinkedIn_Email = os.environ["LinkedIn_Account"]
LinkedIn_Password = os.environ["LinkedIn_Pwd"]
chrome_driver_path = "C:\\Dev\\chromedriver.exe"


def launchBrowser():
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("https://linkedin.com/")
    
    sign_in(driver)
    search_jobs(driver)
    while(True):
        pass


def sign_in(driver):        
    '''input_email'''
    driver.find_element(By.ID, "session_key").send_keys(LinkedIn_Email)
    '''input_password'''
    driver.find_element(By.ID, "session_password").send_keys(LinkedIn_Password)
    '''click_submit/sign-in'''    
    driver.find_element(By.CLASS_NAME,"sign-in-form__submit-button").click()

def search_jobs(driver):
    time.sleep(3)
    '''search_button'''
    driver.find_element(By.CLASS_NAME,"search-global-typeahead__collapsed-search-button").click()
    
    search = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
    search.send_keys("DevOps")
    search.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[ text() = "See all job results in Canada" ]').click()
    
    
    


def apply_jobs():
    pass

launchBrowser()
