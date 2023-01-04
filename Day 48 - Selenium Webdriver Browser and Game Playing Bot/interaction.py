from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\\Dev\\chromedriver.exe"

def launchBrowser():
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    #count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text #XPath
    #count = driver.find_element(By.CSS_SELECTOR, "#articlecount a") #CSS SElector
    # print(count.text)
    # count.click()
    
    search = driver.find_element(By.NAME , "search")
    search.send_keys("Python")
    
    """Can use the search action by either using submit method or using the Keys class"""
    search.submit()
    #search.send_keys(Keys.ENTER)
    while True:
        pass
    
    
launchBrowser()

