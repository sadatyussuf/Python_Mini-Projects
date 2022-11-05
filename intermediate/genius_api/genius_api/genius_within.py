from lyricsgenius import Genius
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get('GENIUS_ACCESS_TOKEN')


class TheGeniusWithin(Genius):
    def __init__(self, client_token=token, close=False):
        self.client_token = client_token
        self.close = close
        print(token)

        super().__init__(access_token=token)
        # .access_token(token)
        # self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     if self.close:
    #         self.quit()

    def get_artist(self, artist, max_songs=3, sort='title'):
        artist = self.search_artist(artist, max_songs=max_songs, sort=sort)
        print(artist)
