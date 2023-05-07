from lightnovel import LightNovelScrapper

with LightNovelScrapper() as bot:
    bot.landing_page()
    bot.select_genre('action')
    bot.refresh()
    bot.collect_results(20)
