from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


s=Service('C:/Users/borov/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/")
driver.set_window_size(1366, 768)
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "login-otp-button").click()
exitbutton = driver.find_element(By.ID, "logout-button")
if exitbutton is None:
    print("Элемента нет")
else:
    print("Элемент есть")
time.sleep(5)