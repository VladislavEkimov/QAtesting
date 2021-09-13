import os

from selenium import webdriver
import time
import math


try:
     browser = webdriver.Chrome()
     url = 'http://suninjuly.github.io/redirect_accept.html'
     browser.get(url)

     button = browser.find_element_by_css_selector("[type='submit']")
     button.click()

     new_window = browser.window_handles[1]
     browser.switch_to.window(new_window)

     x = int(browser.find_element_by_css_selector('#input_value').text)
     result = str(math.log(abs(12*math.sin(x))))

     input = browser.find_element_by_css_selector('.form-control')
     input.send_keys(result)

     button = browser.find_element_by_css_selector('.btn')
     button.click()

finally:
    time.sleep(5)
    browser.quit()