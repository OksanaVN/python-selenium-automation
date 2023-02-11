from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service


service = Service('C:/User/soxano/Documents/Automation/python-selenium-automation/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

sleep(5)

driver.find_element(By.ID, 'nav-orders').click()

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text


assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

print('Test Case passed')


#By Email
# email_input = driver.find_element(By.ID, 'ap_email')
#
# assert email_input.is_displayed(), "Email input field not found or not displayed"
#
# print('Test Case passed')

#print(actual_result)

#Lana's version
# assert driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'
#
# print('Test Case passed')
#
# driver.quit()



