# Amazon logo

driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
# or

driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo' and @aria-label='Amazon']")


# Email

driver.find_element(By.XPATH, //input[@type='email']")

# Email by Id

driver.find_element(By.ID, 'ap_email')


#Continue button

driver.find_element(By.XPATH, "//input[@class='a-button-input']")

#Continue button by Id

driver.find_element(By.ID, 'continue')


#Need help link

driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#Forgot your password link by Id

driver.find_element(By.ID, 'auth-fpp-link-bottom')


#Other issues with Sign-In link by Id

driver.find_element(By.ID, 'ap-other-signin-issues-link')

#Other issues with Sign-In link by XPATH

driver.find_element(By.XPATH, "//a[@class='a-link-normal' and @href='/gp/help/customer/account-issues/ref=ap_login_with_otp_claim_collection?ie=UTF8']")

#Create your Amazon account button by Id

driver.find_element(By.ID, 'createAccountSubmit')

#Create your Amazon account button by XPATH

driver.find_element(By.XPATH, "//a[@class='a-button-text']")


# *Conditions of use link
driver.find_element(By.XPATH, "//a[@class='a-link-normal' and @href='/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId=508088']")

# *Privacy Notice link

driver.find_element(By.XPATH, "//a[@class='a-link-normal' and @href='/gp/help/customer/display.html/ref=ap_desktop_footer_privacy_notice?ie=UTF8&nodeId=468496']")