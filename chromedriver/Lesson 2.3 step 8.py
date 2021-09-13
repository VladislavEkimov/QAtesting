import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
     browser = webdriver.Chrome()
     link = 'http://suninjuly.github.io/explicit_wait2.html'
     browser.get(link)

     buttonBook = browser.find_element_by_css_selector('.btn')

     price = WebDriverWait(browser, 12).until(
          EC.text_to_be_present_in_element((By.ID, "price"), "100")
     )
     buttonBook.click()

     x = int(browser.find_element_by_css_selector('#input_value').text)
     result = str(math.log(abs(12*math.sin(x))))

     input = browser.find_element_by_css_selector('.form-control')
     input.send_keys(result)

     print(x)

     button = browser.find_element_by_css_selector('#solve')
     button.click()

finally:
     time.sleep(15)
     browser.quit()