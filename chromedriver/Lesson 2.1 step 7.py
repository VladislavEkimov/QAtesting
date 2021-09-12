
from selenium import webdriver
import time
import math

try:
    url = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element_by_css_selector('#treasure')
    textX = int(x.get_attribute('valuex'))
    print(textX)

    result = str(math.log(abs(12 * math.sin(textX))))
    print(result)

    inputResult = browser.find_element_by_css_selector('#answer')
    inputResult.send_keys(result)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    radioButton = browser.find_element_by_css_selector('#Lesson 2.1 step 5.pyrobotsRule')
    radioButton.click()

    button = browser.find_element_by_css_selector('.btn-default')
    button.click()


finally:
    time.sleep(5)
    browser.quit()