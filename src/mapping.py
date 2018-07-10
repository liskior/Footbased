from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Mapping(object):
    plots = ["mg_line_plot", "mg_histogram", "mg_scatter"]
    active = 0
    list = False

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "/usr/bin/chromium-browser"
        self.__driver = webdriver.Chrome('./chromedriver')
        self.__driver.get('http://127.0.0.1:5000/mg')

    def open_list(self):
        print(self.__driver)
        python_button = self.__driver.find_elements_by_xpath("//button[@id='filter_0']")[0]
        python_button.click()
        list = True

    def click(self, n):
        if self.list:
            self.open_list()
        self.list = False
        python_button1 = self.__driver.find_elements_by_xpath("//li[@role='presentation']")[n]
        python_button1.click()
        self.hide()

    def __del__(self):
        self.__driver.quit()

    def next(self):
        script = "document.getElementById('" + self.plots[self.active] + "').firstChild.style.height='0'"
        self.__driver.execute_script(script)
        self.active = (self.active + 1) % 3
        script = "document.getElementById('" + self.plots[self.active] + "').firstChild.style.height='200'"
        self.__driver.execute_script(script)

    def choose(self, n):
        python_button = self.__driver.find_elements_by_xpath("//li[@role='presentation']")[n]
        hover = ActionChains(self.__driver).move_to_element(python_button)
        hover.perform()

    def hide(self):
        self.__driver.execute_script("document.getElementById('mg_histogram').firstChild.style.height='0'")
        self.__driver.execute_script("document.getElementById('mg_scatter').firstChild.style.height='0'")

