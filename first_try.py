# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 17:24:56 2016

@author: Nikolay_Semyachkin
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def upload_predictions(filename):
    driver.find_element_by_id('hiddenFileUpload').send_keys(os.getcwd()+ '/' + filename)
    
    


with open('auth.txt') as f:
    email = f.readline()
    passw = f.readline()

driver = webdriver.Chrome()
driver.get("https://numer.ai/login")
login = driver.find_element_by_xpath("//input[@type='email']")
password = driver.find_element_by_xpath("//input[@type='password']")

login.send_keys(email)
password.send_keys(passw)

password.submit()
time.sleep(5)
upload_predictions('dummy_log_regr.csv')