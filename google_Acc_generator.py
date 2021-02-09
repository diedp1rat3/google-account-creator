from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome('chromedriver.exe') 

driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")


namestr = input(str("Enter name:"))
name = driver.find_element_by_name('firstName')
name.click()
name.send_keys(namestr)


surnamestr = input(str("Enter surname:"))
surname = driver.find_element_by_name('lastName')
surname.click()
surname.send_keys(surnamestr)

gmailnamestr = input(str("Enter email name:"))
gmail = driver.find_element_by_name('Username')
gmail.click()
gmail.send_keys(gmailnamestr)

passwordstr = input(str("Enter account password:"))
password = driver.find_element_by_name('Passwd')
password.click()
password.send_keys(passwordstr)

passwordverify = driver.find_element_by_name('ConfirmPasswd')
passwordverify.click()
passwordverify.send_keys(passwordstr)

print ("Press button to continue...")

phonenumberstr = input(str("Enter your phone number:"))
phonenumber = driver.find_element_by_id('phoneNumberId')
phonenumber.click()
phonenumber.send_keys(phonenumberstr)

time.sleep(3)
print("Press button to continue")

time.sleep(3)

codestr = input(str("Enter message you got from phone"))
code = driver.find_element_by_id('code') 
code.click()
code.send_keys(codestr)

time.sleep(1)

print("Please press button to continue.")

yearstr = input(int("What year you we're born?"))
year = driver.find_element_by_name('year')
year.click()
year.send_keys(yearstr)

time.sleep(3)
print("Please select month you we're born")

daystr = input(int("What day you we're born?"))
day = driver.find_element_by_name('year')
day.click() 
day.send_keys(daystr)

time.sleep (3)

print ("Please select your gender.")

time.sleep(3)

print("Please press button to continue")

time.sleep(3)

print("Please press button to continue.")

time.sleep(3)
 
print("Please select you need and press button")

time.sleep(3)

print("Please press button to continue.")

time.sleep(3) 

print("Please press button to continue.")

print("You're done !")