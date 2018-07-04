from selenium import webdriver
import time

driver = None

def open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    driver = webdriver.Chrome('/Users/asya/Downloads/chromedriver')
    driver.get('http://127.0.0.1:5000/mg')
    time.sleep(5)
    open_list()
    time.sleep(5)
    click(2)
    time.sleep(5)
    open_list()
    time.sleep(5)
    click(3)
    time.sleep(5)


def open_list():
    python_button = driver.find_elements_by_xpath("//button[@id='filter_0']")[0]
    python_button.click()


def click(n):
    python_button1 = driver.find_elements_by_xpath("//li[@role='presentation']")[n]
    python_button1.click()


open_browser()