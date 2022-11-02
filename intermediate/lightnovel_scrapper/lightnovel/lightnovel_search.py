from selenium import webdriver
from rich import print as rprint
import os


class LightNovelScrapper(webdriver.Chrome):
    def __init__(self, driver=r'C:\SeleniumDrivers'):
        self.driver = driver

        os.environ['PATH'] += self.driver
        super(LightNovelScrapper, self).__init__()
        self.implicitly_wait(30)

    def test_url(self):
        self.get('http://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')

        btn = self.find_element(
            by='css selector',
            value= '#downloadButton'
        )
        btn.click()




