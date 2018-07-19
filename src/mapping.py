from os.path import lexists
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Mapping(object):

    active = 0
    __list = [False, False, False]
    crutch = [0, 5, 8]

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "/usr/bin/chromium-browser"

        # Asia, schreib ./chromedriver in CHROME_DRV_PATH.txt
        # CHROME_DRV_PATH.txt ist in .gitignore
        f = open('CHROME_DRV_PATH.txt', 'r')
        drvpath = f.readline().rstrip()
        chromedriver_path = drvpath
        f.close()

        self.__driver = webdriver.Chrome(chromedriver_path)
        self.__driver.get('http://127.0.0.1:5000/mg')
        self.show(0)
        sleep(2)
        self.show(1)

        sleep(2)
        self.show(2)

    def open_list(self, id):
        if self.active != id:
            return
        print(self.__driver)
        python_button = self.__driver.find_elements_by_xpath("//button[@id='filter_" + str(id) + "']")[0]
        python_button.click()
        self.__list[id] = True

    def click(self, n, id):
        if self.active != id:
            return
        if not self.__list[id]:
            self.open_list(id)

        self.__list[id] = False
        python_button1 = self.__driver.find_elements_by_xpath("//li[@role='presentation']")[self.crutch[self.active] + n]
        python_button1.click()

    def __del__(self):
        self.__driver.quit()

    def choose(self, n):
        python_button = self.__driver.find_elements_by_xpath("//li[@role='presentation']")[self.crutch[self.active] + n]
        hover = ActionChains(self.__driver).move_to_element(python_button)
        hover.perform()

    def show(self, i):
        for j in range(3):
            if j != i:
                script = "document.getElementsByClassName('btn-group')[" + str(j) + "].style.display='none'"
                self.__driver.execute_script(script)
            else:
                script = "document.getElementsByClassName('btn-group')[" + str(j) + "].style.display='inline-block'"
                self.__driver.execute_script(script)
        self.click(self.crutch[i] + 1, i)
        self.active = i
