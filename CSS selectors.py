from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path='C:/User/soxano/Documents/Automation/python-selenium-automation/chromedriver.exe')

driver.get('https://www.amazon.com/')

#By Id

driver.find_element(By.ID, 'twotabsearchtextbox')

#By CSS using ID

driver.find_element(By.CSS_ELECTOR, '#twotabsearchtextbox')

#By CSS, using class

driver.find_element(By.CSS_ELECTOR, 'span.icp-nav-flag-us')
driver.find_element(By.CSS_ELECTOR, '.icp-nav-flag-us')

#multiple classes
driver.find_element(By.CSS_ELECTOR, 'span.icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop')

#Using attriibutes, except Id and Class
driver.find_element(By.CSS_ELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.CSS_ELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")

#multiple attributes

driver.find_element(By.CSS_ELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers'][tabindex='0']")

#Class and Attributes

driver.find_element(By.CSS_ELECTOR, "a.nav-a[data-csa-c-content-id='nav_cs_bestsellers'][tabindex='0']")

# Attributes partial match *=
driver.find_element(By.CSS_ELECTOR, "a[href*='ref_=nav_cs_bestsellers']")

# CSS, from parent to child
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*=condition_of_use]")
driver.find_element(By.CSS_SELECTOR, "div.a-section #legalTextRow a[href*=condition_of_use]")

#Xpath backwards from child to a parent
driver.find_element(By.XPATH, "//*[./a[contains(@href, 'ap_signin_notification_condition_of_use')]]")
