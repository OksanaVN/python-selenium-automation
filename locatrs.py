from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome(executable_path='C:/User/soxano/Documents/Automation/python-selenium-automation/chromedriver.exe')

driver.get('https://www.amazon.com/')

#By Id

driver.find_element(By.ID, 'twotabsearchtextbox')

#By Xpath, tag and attribute

driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")

#By Xpath, multiple atributes

driver.find_element(By.XPATH, "//a[@aria-label='Amazon' and @href='/ref=nav_logo']")
driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers' and @data-csa-c-content-id='nav_cs_bestsellers' and @data-csa-c-type='link']")

#By Xpath, contains:
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")
# contains AND atr
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers') and @data-csa-c-type='link']")


#By Xpath, without a tag

driver.find_element(By.XPATH, "//*[contains(@href, 'nav_cs_bestsellers') and @data-csa-c-type='link']")
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']")

#By Xpath, attr starts with certain vaue:
driver.find_element(By.XPATH, '//a[starts-with(@href, "/gp/bestsellers/?")]')


#By Xpath text
driver.find_element(By.XPATH, "//h2[text()='The warm-weather edit']")
driver.find_element(By.XPATH, "//h2[contains(text(), 'The warm-weather')]")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class ='nav-a ']")

#By Xpath, goin from parent node to child

driver.find_element(By.XPATH, "//div[@id='nav-xshop']//a[text()='Best Sellers']")


