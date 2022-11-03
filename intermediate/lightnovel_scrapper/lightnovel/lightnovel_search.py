import os

import pandas as pd
from selenium import webdriver

from lightnovel import constants as const


class LightNovelScrapper(webdriver.Chrome):
    def __init__(self, driver=r'C:\SeleniumDrivers', close=False):
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

    def select_genre(self, genre):
        genre_btn = self.find_element(
            by='css selector',
            # value='#hot-genre-select'
            value='.list-genre .row'
        )

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
                break

    def collect_results(self, result_num):
        collections = []
        main = self.find_element(
            by='css selector',
            value='.col-novel-main .list-novel'
        )

        novel_list = main.find_elements(
            by='css selector',
            value='.row'
        )
        c = 0
        for novel in novel_list:
            if c >= result_num:
                break
            novel_img = novel.find_element(
                by='css selector',
                value='img'
            ).get_attribute('src')

            novel_title = novel.find_element(
                by='css selector',
                value='.novel-title a'
            ).get_attribute('innerHTML').strip().lower()

            novel_author = novel.find_element(
                by='css selector',
                value='.author'
            ).text
            # .get_attribute('textContent').strip().lower()

            novel_chapter_info = novel.find_element(
                by='css selector',
                value='.text-info span'
            ).get_attribute('innerHTML').strip().lower()

            collections.append({
                'novel_img': novel_img,
                'novel_title': novel_title,
                'novel_author': novel_author,
                'novel_chapter_info': novel_chapter_info})
            # collections.append([novel_img, novel_title, novel_author, novel_chapter_info])

            c += 1
        dataframe = pd.DataFrame(collections)
        dataframe.to_csv('results.csv')
        # rprint(main.get_attribute('innerHTML'))
        # while c < result_num:
        # headers = ['novel_img', 'novel_title', 'novel_author', 'novel_chapter_info']
        # print(pd.DataFrame(collections, headers, headers))
        # print('                                         ')
        print('-----------------------------------------')
        # print('                                         ')
        # print(pd.DataFrame(collections, headers))
        # rprint(tabulate(collections, headers))
