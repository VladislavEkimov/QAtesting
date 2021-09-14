import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import keys


class TestYandex(unittest.TestCase):

    def testInput(self):
        browser = webdriver.Chrome()
        link = 'https://yandex.ru/'
        browser.get(link)
        if browser.find_elements_by_xpath('//*[@id="text"]'):
            input = True
        else:
            input = False
        self.assertEqual(input, True, 'No input field')

    def testSearch(self):
        browser = webdriver.Chrome()
        link = 'https://yandex.ru/'
        browser.get(link)
        input = browser.find_element_by_xpath('//*[@id="text"]')
        input.send_keys('тензор')

        if browser.find_element_by_css_selector("[role='listbox']"):
            suggest = True
        else:
            suggest = False
        self.assertEqual(suggest, True, 'No suggest field')

    def testLink(self):
        browser = webdriver.Chrome()
        link = 'https://yandex.ru/'
        browser.get(link)
        input = browser.find_element_by_xpath('//*[@id="text"]')
        input.send_keys('тензор')
        input.send_keys(keys.Keys.ENTER)







if __name__ == "__main__":
    unittest.main()