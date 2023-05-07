from lyricsgenius import Genius
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get('GENIUS_ACCESS_TOKEN')


class TheGeniusWithin:
    def __init__(self):

        self.genius = Genius(
            token,
            skip_non_songs=True,
            excluded_terms=["(Remix)", "(Live)"],
            remove_section_headers=True
        )

    def get_artist(self, artist, max_songs=3, sort='popularity'):
        genius = self.genius
        try:
            artist = genius.search_artist(
                artist, max_songs=max_songs, sort=sort).songs
            for i in artist:
                print(i.lyrics)
            # print(artist)
        except:
            raise
