from lyricsgenius import Genius


class TheGeniusWithin(Genius):
    def __init__(self, client_token):
        self.client_token = client_token

        super().__init__(access_token=self.client_token)
        pass
