
from selenium import webdriver
import time
import math

from selenium.webdriver.support.select import Select

try:
     url = 'http://suninjuly.github.io/selects1.html'
     browser = webdriver.Chrome()
     browser.get(url)

     num1 = int(browser.find_element_by_css_selector('#num1').text)
     num2 = int(browser.find_element_by_css_selector('#num2').text)

     result = str(num1+num2)

     select = Select(browser.find_element_by_css_selector('#dropdown'))
     select.select_by_value(result)

     button = browser.find_element_by_css_selector('.btn')
     button.click()

finally:
    time.sleep(5)
    browser.quit()