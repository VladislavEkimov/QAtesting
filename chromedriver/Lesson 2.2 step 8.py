import os

from selenium import webdriver
import time
import math


try:
     browser = webdriver.Chrome()
     url = 'http://suninjuly.github.io/file_input.html'
     browser.get(url)

     inputFirstname = browser.find_element_by_css_selector('[name="firstname"]')
     inputFirstname.send_keys('Vladislav')

     inputLastname = browser.find_element_by_css_selector("[name='lastname']")
     inputLastname.send_keys('Ekimov')

     inputEmail = browser.find_element_by_css_selector("[name='email']")
     inputEmail.send_keys('vladis27449@yandex.ru')

     current_dir = os.path.abspath(os.path.dirname(__file__))
     file_path = os.path.join(current_dir, 'file.txt')
     inputFile = browser.find_element_by_css_selector("[name='file']")
     inputFile.send_keys(file_path)

     button = browser.find_element_by_css_selector('.btn')
     button.click()

finally:
    time.sleep(5)
    browser.quit()