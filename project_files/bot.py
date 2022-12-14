from project_files.link import URL

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


class Google(webdriver.Chrome):
    def __init__(self, driver_path='D:\projekty\Rescue health\chromedriver',
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Google, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')


    def exit(self):
        self.quit()

    def land_first_page(self):
        self.get(URL)

    def accept(self):
        accept = self.find_element(By.XPATH,
        "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 Nc7WLe']"
        )
        accept.click()

    def route(self, first_place, destination):
        self.implicitly_wait(60)
        inputs = self.find_elements(By.XPATH,
        "//input[@class='tactile-searchbox-input']"
        )
        inputs[0].send_keys(first_place)
        inputs[0].send_keys(Keys.ENTER)
        self.implicitly_wait(10)
        inputs[1].send_keys(destination, first_place)
        inputs[1].send_keys(Keys.ENTER)
        

    def route_foot(self):
        time.sleep(5)
        button = self.find_element(By.XPATH,
        "//div[@data-travel_mode='2']/button"
        )
        button.click()
        time.sleep(2)
        self.implicitly_wait(10)
        button = self.find_element(By.XPATH,
        "//h1[@class='VuCHmb fontHeadlineSmall']"
        )
        button.click()
    
    def route_car(self):
        time.sleep(5)
        button = self.find_element(By.XPATH,
        "//div[@data-travel_mode='0']/button"
        )
        button.click()
        time.sleep(2)
        self.implicitly_wait(10)
        button = self.find_element(By.XPATH,
        "//span[@class='JxBYrc pk9Qwb']"
        )
        button.click()


    def route_url(self):
        next_element = self.find_element(By.XPATH,
        "//button[@class='J45yZc ftEYtf']"
        )
        next_element.click()
        self.implicitly_wait(10)
        link = self.find_element(By.XPATH,
        "//input[@class='vrsrZe']"
        ).get_attribute('value')
        return link

