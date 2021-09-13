from selenium import webdriver
import time
import math


try:
     browser = webdriver.Chrome()
     link = "http://suninjuly.github.io/execute_script.html"
     browser.get(link)

     x = int(browser.find_element_by_css_selector('#input_value').text)

     result =  math.log(abs(12*math.sin(x)))

     browser.execute_script("window.scrollBy(0, 200);")

     input = browser.find_element_by_css_selector('#answer')
     input.send_keys(str(result))

     checkbox = browser.find_element_by_css_selector('#robotCheckbox')
     checkbox.click()

     radiobutton = browser.find_element_by_css_selector('#robotsRule')
     radiobutton.click()

     button = browser.find_element_by_css_selector('.btn')
     button.click()

finally:
    time.sleep(5)
    browser.quit()