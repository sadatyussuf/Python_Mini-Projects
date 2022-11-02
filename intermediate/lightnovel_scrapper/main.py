from lightnovel import LightNovelScrapper
from rich import print as rprint

# test = LightNovelScrapper()
# test.test_url()
with LightNovelScrapper() as bot:
    bot.landing_page()
    bot.select_genre('action')
    bot.refresh()
