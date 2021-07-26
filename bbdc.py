#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# selenium for web driving
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver = r"C:\Users\angsh\Downloads\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

# Open the website
driver.get('https://info.bbdc.sg/members-login/')

#let page load
wait = WebDriverWait(driver,60)

#login
username = wait.until(EC.presence_of_element_located((By.ID,"txtNRIC")))
password = wait.until(EC.presence_of_element_located((By.ID,"txtPassword")))
                      
username.send_keys("T0122742J")
password.send_keys("051319")

wait.until(EC.element_to_be_clickable((By.ID,"loginbtn"))).click()
wait.until(EC.element_to_be_clickable((By.ID,"proceed-button"))).click()

#Locate booking without fixed instructor button
driver.switch_to_frame("leftFrame")
driver.find_element_by_xpath("//html/body/table/tbody/tr/td/table/tbody/tr[15]/td[3]/a").click()

#click I Agree
driver.switch_to.default_content()

driver.switch_to_frame("mainFrame")
driver.find_element_by_xpath("//html/body/table/tbody/tr[3]/td[1]/input").click()

#month
driver.find_element_by_xpath("//html/body/table/tbody/tr/td[2]/form/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td[1]/input").click()
driver.find_element_by_xpath("//html/body/table/tbody/tr/td[2]/form/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td[2]/input").click()


#days
driver.find_element_by_xpath("//html/body/table/tbody/tr/td[2]/form/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/input[9]").click()
#sessions
driver.find_element_by_xpath("//html/body/table/tbody/tr/td[2]/form/table/tbody/tr[1]/td/table/tbody/tr[6]/td[2]/input").click()

run_prog = True
while run_prog:
    #search
    driver.find_element_by_xpath("//html/body/table/tbody/tr/td[2]/form/table/tbody/tr[3]/td[2]/input").click()

    #click pop up
    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    
    driver.switch_to.default_content()

    driver.switch_to_frame("mainFrame")
    
    l = list(driver.find_elements_by_xpath("//html/body/table/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/input"))
    s = len(l)

    if s > 0:
    #refresh
        driver.find_element_by_xpath("//html/body/table/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/input").click()
        
    else:
        wait.until(EC.visibility_of_element_located((By.NAME, "slot")))

        # 0 refers to first slot, 1 refers to second slot, and so on...
        slots = driver.find_elements_by_name('slot')
        for slot in slots:     # Selecting all checkboxes
            slot.click()
            driver.find_element_by_class_name('pgtitle').click()     # clicking random element to hide hover effect

        # Selecting Submit
        driver.find_element_by_name('btnSubmit').click()

        # Selecting confirm
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Confirm']")))
        driver.find_element_by_xpath("//input[@value='Confirm']").click()

        import winsound
        duration = 10000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)

