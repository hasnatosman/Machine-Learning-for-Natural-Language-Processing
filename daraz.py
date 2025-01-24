# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# from selenium.webdriver.common.by import By

# driver.get('https://www.daraz.com.bd/routers/')
# driver.maximize_window()
# link = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/a')
# print(link.get_attribute('href'))
# driver.get(link.get_attribute('href'))
# time.sleep(10)
# driver.quit()

from selenium import webdriver
import time
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

driver.get('https://www.daraz.com.bd/routers/')
driver.maximize_window()

link_list = []
for i in range(1,41):
    type_i = str(i)

    # link = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+type_i+']/div/div/div[2]/div[2]/a').get_attribute('href')
    # link_list.append(link)
    link = driver.find_element(By.CSS_SELECTOR, '#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child('+type_i+') > div > div > div.buTCk').get_attribute('href')
    link_list.append(link)


print(link_list)

# print(link.get_attribute('href'))
# driver.get(link.get_attribute('href'))


time.sleep(3)
driver.quit()
