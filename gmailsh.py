from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pg
import time
import random
driver = webdriver.Firefox()
driver.get('https://www.google.com/intl/pt-PT/gmail/about/')
login = driver.find_element_by_xpath("/html/body/nav/div/a[2]")
login.click()
elem = driver.find_element_by_name("identifier")
elem.send_keys('craftmine')
f_t_p = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/content/span')
f_t_p.click()
time.sleep(2)
try:
    pw = driver.find_element_by_name("password")
    pw.send_keys('minecraft')
except:
    pw = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/content/form/div[1]/div/div[1]/div/div[1]/input')
    pw.send_keys('cavaco1974nunoelua')

ftp2 = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/content/span')
ftp2.click()
while True:
    accept = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/span/div')
    accept.click()
    time.sleep(2)
    trash = driver.find_elemet_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div/div[2]/div[3]/div')
    trash.click()
    time.sleep(2)
    
#/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/div/div[1]/span/div
