from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
active = 0
plots = ["mg_line_plot", "mg_histogram", "mg_scatter"]

def open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    driver = webdriver.Chrome('src/chromedriver')
    driver.get('http://127.0.0.1:5000/mg')
    time.sleep(1)
    driver.execute_script("document.getElementById('mg_histogram').firstChild.style.height='0'")
    driver.execute_script("document.getElementById('mg_scatter').firstChild.style.height='0'")
    time.sleep(5)
    #open_list(driver)
    time.sleep(5)
    open_list(driver)
    #click(driver, 2)
    #time.sleep(5)
    #open_list(driver)
    #time.sleep(5)
    #click(driver, 3)
    #time.sleep(5)
    #driver.quit()



def open_list(driver):
    python_button = driver.find_elements_by_xpath("//button[@id='filter_0']")[0]
    hover = ActionChains(driver).move_to_element(python_button)
    hover.perform()
    time.sleep(2)
    python_button.click()
    print("egj")
    print(python_button.size)
    driver.execute_script("document.getElementById('mg_line_plot').firstChild.style.height='0'")
    #driver.execute_script("arguments[0].setAttribute('height', '0')", python_button)
    time.sleep(10)



def next(driver, n):
    global active
    script = "document.getElementById('" + plots[active] + "').firstChild.style.height='0'"
    driver.execute_script(script)
    active = (active + 1) % 3
    script = "document.getElementById('" + plots[active] + "').firstChild.style.height='200'"
    driver.execute_script(script)


def click(driver, n):
    python_button = driver.find_elements_by_xpath("//li[@role='presentation']")[n]
    python_button.click()

def choose(driver, n):
    python_button = driver.find_elements_by_xpath("//li[@role='presentation']")[n]
    hover = ActionChains(driver).move_to_element(python_button)
    hover.perform()


open_browser()

