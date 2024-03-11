import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://www.getcalley.com/page-sitemap.xml")
driver.maximize_window()

driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR,"a[href='https://www.getcalley.com/']").click()
driver.save_screenshot("C:\Screenshot\first.png")
driver.back()

driver.find_element(By.CSS_SELECTOR,"a[href='https://www.getcalley.com/calley-call-from-browser/']").click()
driver.save_screenshot("C:\Screenshot\second.png")
driver.back()

driver.find_element(By.CSS_SELECTOR,"a[href='https://www.getcalley.com/calley-pro-features/']").click()
driver.save_screenshot("C:\Screenshot\third.png")
driver.back()

driver.find_element(By.CSS_SELECTOR,"a[href='https://www.getcalley.com/best-auto-dialer-app/']").click()
driver.save_screenshot("C:\Screenshot\fourth.png")
driver.back()

driver.find_element(By.CSS_SELECTOR,"a[href='https://www.getcalley.com/how-calley-auto-dialer-app-works/']").click()
driver.save_screenshot("C:\Screenshot\fifth.png")
driver.back()

driver.close()