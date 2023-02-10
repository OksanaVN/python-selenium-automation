from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service


#driver = webdriver.Chrome(executable_path='C:/User/soxano/Documents/Automation/python-selenium-automation/chromedriver.exe')

service = Service('C:/User/soxano/Documents/Automation/python-selenium-automation/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

sleep(5)

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"table"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
print(actual_result)

assert expected_result ==actual_result, f'Expected {expected_result} but got actual {actual_result}'
print('Test Case passed')

driver.quit()
