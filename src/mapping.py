from selenium import webdriver
import time

def open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    driver = webdriver.Chrome('/Users/asya/Downloads/chromedriver')
    driver.get('http://127.0.0.1:5000/mg')
    print(driver)
    time.sleep(5)
    open_list(driver)
    time.sleep(5)
    click(driver, 2)
    time.sleep(5)
    open_list(driver)
    time.sleep(5)
    click(driver, 3)
    time.sleep(5)
    driver.quit()


def open_list(driver):
    print(driver)
    python_button = driver.find_elements_by_xpath("//button[@id='filter_0']")[0]
    python_button.click()


def click(driver, n):
    python_button1 = driver.find_elements_by_xpath("//li[@role='presentation']")[n]
    python_button1.click()


open_browser()