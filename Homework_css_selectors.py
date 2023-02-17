from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path='C:/User/soxano/Documents/Automation/python-selenium-automation/chromedriver.exe')

driver.get('https://www.amazon.com/')

#Siince the task of HW3 says to find most optimal locators I used IDs when they were available, in other places I practiced with CSS locators.


#Amazon logo by class

driver.find_element(By.CSS_ELECTOR, 'i.a-icon.a-icon-logo')

#Create accunt by class

driver.find_element(By.CSS_ELECTOR, 'h1.a-spacing-small')

# Your name input field

driver.find_element(By.ID, 'ap_customer_name')

# Mobile number or email input field

driver.find_element(By.ID, 'ap_email')

# Password input field

driver.find_element(By.ID, 'ap_password')

# Re-enter password input field

driver.find_element(By. ID, 'ap_password')

# Continue button

driver.find_element(By.ID, 'ap_password')

# Conditions of use link

driver.find_element(By.CSS_SELECTOR, "a[href*='ref=ap_register_notification_condition_of_use']")

# Privacy notice link

driver.find_element(By.CSS_SELECTOR, "a[href*='ref=ap_register_notification_privacy_notice']")

# Sign in link

driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?openid.pape.max_auth_age=0']")

