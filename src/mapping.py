""" GUI

This gives us a GUI, on which we can define actions, to which we can map foot
movements.

"""

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Mapping(object):

    active = 0 # active LIST
    __list = [False, False, False] # list open
    crutch = [0, 5, 8]


    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "/usr/bin/chromium-browser"


        # Write the path to your installation of chromedriver into this file.
        # It is .gitignore-d, therefore unique to your computer.
        f = open('CHROME_DRV_PATH.txt', 'r')
        drvpath = f.readline().rstrip()
        chromedriver_path = drvpath
        f.close()

        self.__driver = webdriver.Chrome(chromedriver_path)
        self.__driver.get('http://127.0.0.1:5000/mg')

        self.click(0, 0)
        self.current_list = 0
        self.current_item = 0

    def open_list(self, a):
        if self.active != a:
            return
        print(self.__driver)
        python_button = self.__driver.find_elements_by_xpath("//button[@id='filter_" + str(a) + "']")[0]
        python_button.click()
        self.__list[a] = True

    def next_list(self):
        self.current_list += 1
        self.current_list %= 3
        self.open_list()


    def click(self, n, a):
        """
        n: ITEM IN A LIST  id
        a: LIST BUTTON id
        """
        self.current_list = a
        self.current_item = n

        if self.active != a:
            return
        if not self.__list[a]:
            self.open_list(a)
        self.__list[a] = False
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
        self.active = i
        self.click(1, i)

