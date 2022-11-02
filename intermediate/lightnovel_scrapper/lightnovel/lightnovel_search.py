from selenium import webdriver
from rich import print as rprint
import os
from lightnovel import constants as const


class LightNovelScrapper(webdriver.Chrome):
    def __init__(self, driver=r'C:\SeleniumDrivers',close=False):
        self.driver = driver
        self.close = close

        os.environ['PATH'] += self.driver
        super(LightNovelScrapper, self).__init__()
        self.implicitly_wait(30)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.close:
            self.quit()

    def landing_page(self):
        self.get(const.BASE_URL)

    def select_genre(self,genre):
        genre_btn = self.find_element(
            by='css selector',
            # value='#hot-genre-select'
            value='.list-genre .row'
        )
        # genre_btn.click()

        genre_options = genre_btn.find_elements(
            by='css selector',
            # value= 'option'
            value='div'
        )
        for option in genre_options:
            option_text = option.find_element(
                by='css selector',
                value='a'
            ).get_attribute('innerHTML').strip().lower()
            if option_text == genre:
                option.click()
                # break







