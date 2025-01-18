from selenium import webdriver
import time
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

driver.get('https://www.daraz.com.bd/routers/')
driver.maximize_window()
link = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/a')
print(link.get_attribute('href'))
driver.get(link.get_attribute('href'))
time.sleep(10)
driver.quit()