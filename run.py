from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from random import random
from getIdPass import getIdPass
import time

#Menu
print("\nPress 1: for Sandeep")
print("Press 2: for Bhupendra")
print("Press 3: for Hemant\n")
a = int(input("Enter your choice: "))

#assigning selenium webdriver to browser
browser = webdriver.Chrome(service=Service("C:\\Users\\sande\\Desktop\\Programs\\Projects\\linkedin-request-sender\\chromedriver.exe"))
browser.get('https://in.linkedin.com/')
browser.maximize_window()
time.sleep(2)


def login():
    #get email and password
    email = getIdPass(a)[0].strip("email_id=")
    password = getIdPass(a)[1].strip("password=")

    #click on sign_in button
    browser.find_element(By.LINK_TEXT, 'Sign in').click()
    time.sleep(3)

    #enter email and password
    email_btn = browser.find_element(By.CSS_SELECTOR, '#username')
    email_btn.send_keys(email)
    pass_btn = browser.find_element(By.CSS_SELECTOR, '#password')
    pass_btn.send_keys(password)

    #click on sign_in button
    signin_btn = browser.find_element(By.XPATH, "//button[contains(text(),'Sign in')]")
    signin_btn.click()
    time.sleep(2)


def search():
    #find search bar and type "hr" and search
    search_btn = browser.find_element(By.XPATH, '//input[@placeholder="Search"]')
    str = ["hr", "talent acquisition" ]
    search_btn.send_keys(str[int(random()*2)], Keys.ENTER)
    time.sleep(4)

    #visit show all results page
    browser.get("https://www.linkedin.com/search/results/people/?keywords=hr&origin=CLUSTER_EXPANSION")
    time.sleep(2)


def sendRequest():
    #find all the connect/follow buttons
    connect_btns = browser.find_elements(By.XPATH, "//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")
    #if button is "connect" then click on it
    for items in connect_btns:
        if(items.text == 'Connect'):
            items.click()
            #find the send button and click on it
            send_btn = browser.find_element(By.XPATH, "//button[@aria-label='Send now']")
            send_btn.click()
            time.sleep(1)


def changePage():
    #find next page button and click on it
    for i in range(2, 100):
        sendRequest()
        #get the next page
        pageLink = f"https://www.linkedin.com/search/results/people/?keywords=hr&origin=SWITCH_SEARCH_VERTICAL&page={i}"
        browser.get(pageLink)
        time.sleep(2)
            
login()
search()
changePage()

browser.close()