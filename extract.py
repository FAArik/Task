from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from langdetect import detect
import requests
import time

url="https://www.google.com"
def createDriver() -> webdriver.Chrome:
    

    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    return myDriver

def javascr(driver: webdriver.Chrome,url:str) -> str:
    
    driver.get(url) 
    button = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/nav/div[1]/button[2]")
    actions=ActionChains(driver)
    actions.move_to_element(button)
    actions.perform()
   
    time.sleep(3)
    search = driver.find_element(By.CLASS_NAME, "main-nav-dropdown__index").is_displayed()       
    if(search==1):
        print('found')
        return {"PASS":"Javascript works properly"}
    else:
        print('not found')
        return {"FAIL":"Javascript doesn't works "}


def imageres(driver: webdriver.Chrome,url:str) -> str:
    driver.get(url) 
    img = driver.find_element(By.XPATH, "/html/body/div[1]/main/section[1]/div[1]/img").get_attribute("src")
    response = requests.head(img)
    file_size = int(response.headers.get("Content-Length", 0))
    if (file_size<70000):
        return {"FAIL":"Image is blurred "}
    else:
        return {"PASS":"Image quailty is good "}
    

def language(driver: webdriver.Chrome,url:str) -> str:
    driver.get(url)
    buton=driver.find_element(By.XPATH,"/html/body/div[1]/main/section[1]/div[2]/ul/li[1]")
    text1 = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[1]/div[2]/h2').text
    t1lang=detect(text1)
    buton.click()
    time.sleep(5)
    text2 = driver.find_element(By.TAG_NAME,'body').text
    t2lang=detect(text2)
    if(t2lang!=t1lang):
        return {"FAIL":"Pages doesn't translated properly"}
    else:
        return{"PASS":"Pages translated properly"}


def wrong(driver: webdriver.Chrome,url:str) -> str:
    driver.get(url)
    titles=driver.find_elements(By.TAG_NAME,"title itemprop")
    for title in titles:
        if(detect(title.text)=="en"):
            return {"Fail":"Wrong site"}
        else:
            return {"PASS":"Wrong site"}
    