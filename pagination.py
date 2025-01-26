from selenium import webdriver
import time
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

link_list = []

for page_no in range(1,3):
    driver.get(f'https://www.daraz.com.bd/routers/?page={page_no}')
    driver.maximize_window()
    for prod in range(1,13):
        type_i = str(prod)

        #using x.path

        link = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').get_attribute('href')
        link_list.append(link)

        #using css.selector
        # link = driver.find_element(By.CSS_SELECTOR,'#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child('+type_i+') > div > div > div.buTCk > div.RfADt > a').get_attribute('href')
        # link_list.append(link)
print(link_list)
print(len(link_list))
time.sleep(3)
driver.quit()