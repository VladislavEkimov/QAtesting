import math

from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_tag_name('input')

    for item in elements:
        item.send_keys("Привет")

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:

    time.sleep(10)

    browser.quit()