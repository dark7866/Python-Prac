from selenium import webdriver
import sys
import time

#Only works with hotmail accounts!1

# get user info

email = input("Email:")

password = input("Password: ")

sendTo = input("sendTo:")

subject = input("subject: ")

message = input("message: ")


#navigate to browser
browser = webdriver.Firefox(executable_path=r'/home/rufyi/geckodriver')
browser.get('https://outlook.live.com/owa/')
elem = browser.find_element_by_css_selector('.auxiliary-actions > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)')
elem.click()
emailElem = browser.find_element_by_css_selector('#i0116')

emailElem.send_keys(email)
elem = browser.find_element_by_css_selector('#idSIButton9')
elem.click()

passElem = browser.find_element_by_css_selector('#i0118')


passElem.send_keys(password)

elem = browser.find_element_by_css_selector('#idSIButton9')
elem.click()

time.sleep(2)

elem = browser.find_element_by_css_selector('#id__3')
elem.click()

time.sleep(4)

toElem = browser.find_element_by_css_selector('.ms-BasePicker-input')
toElem.send_keys(sendTo)

bodyElem = browser.find_element_by_css_selector('._4utP_vaqQ3UQZH0GEBVQe')
bodyElem.send_keys(message)

subjectElem = browser.find_element_by_css_selector('#subjectLine0')
subjectElem.send_keys(subject)

elem = browser.find_element_by_css_selector('.ms-Button--primary > span:nth-child(1)')
elem.click()

elem = browser.find_element_by_css_selector('._14ggU2yZvNol5U91gfmYQA > img:nth-child(1)')
elem.click()

elem = browser.find_element_by_css_selector('#meControlSignoutLink')
elem.click()

browser.close()