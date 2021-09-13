import os

from selenium import webdriver
import time
import math


try:
     browser = webdriver.Chrome()
     url = 'http://suninjuly.github.io/alert_accept.html'
     browser.get(url)

     button = browser.find_element_by_css_selector('.btn')
     button.click()

     confirm = browser.switch_to.alert
     confirm.accept()

     x = int(browser.find_element_by_css_selector('#input_value').text)
     result = str(math.log(abs(12*math.sin(x))))

     input = browser.find_element_by_css_selector('#answer')
     input.send_keys(result)

     button = browser.find_element_by_css_selector('.btn')
     button.click()

finally:
    time.sleep(5)
    browser.quit()