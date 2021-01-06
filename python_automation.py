import selenium
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

import time 
driver = webdriver.Chrome('C:\\Users\\Baazigar\\Desktop\\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
time.sleep(20)
print ("abc")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[1]").click()
print ("profile clicked")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div")
print ("footer clicked")
time.sleep(2)
element=driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')

for i in range(1,50):
    msg="the text msg"
    print (element)
    element.click()
    print ("elemenet clicked")
    time.sleep(2)
    print ("going to send msg")
    element.send_keys(msg+Keys.ENTER)
    print ("msg sent")


