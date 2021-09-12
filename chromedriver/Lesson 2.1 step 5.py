
from selenium import webdriver
import time
import math

try:
    url = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(url)

    x = int(browser.find_element_by_css_selector('#input_value').text)
    result = str(math.log(abs(12 * math.sin(x))))

    inputX = browser.find_element_by_css_selector('#answer')
    inputX.send_keys(result)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()

    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()