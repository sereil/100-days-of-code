from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Dev\\chromedriver.exe"
AMAZON_INSTANT_POT = "https://www.amazon.ca/dp/B06Y1MP2PY?ref_=cm_sw_r_cp_ud_dp_KSMTX9CKEFM5XHZ2BCHQ&th=1"

def launchBrowser():
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("https://www.python.org/")
    
    # upcoming_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget div ul li")
    # print(upcoming_events)
    event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
    event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
    events = {}
    for n in range(len(event_times)):
        events[n] = {
            "time":event_times[n].text,
            "name":event_names[n].text        
        }
                
    print(events)
    while(True):
        pass

launchBrowser()
