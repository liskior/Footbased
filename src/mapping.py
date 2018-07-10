from selenium import webdriver
import time

class Mapping(object):

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "/usr/bin/chromium-browser"
        self.__driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        self.__driver.get('http://127.0.0.1:5000/mg')

    def open_list(self):
        print(self.__driver)
        python_button = self.__driver.find_elements_by_xpath("//button[@id='filter_0']")[0]
        python_button.click()


    def click(self, n):
        python_button1 = self.__driver.find_elements_by_xpath("//li[@role='presentation']")[n]
        python_button1.click()

    def __del__(self):
        self.__driver.quit()
