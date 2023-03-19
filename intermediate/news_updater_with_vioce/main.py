from dotenv import load_dotenv
from newsapi import NewsApiClient
import os
import json
import pyttsx3
from pathlib import Path
import uuid

load_dotenv()
BASE_DIR = Path(__file__).parent

token = os.environ.get("NEWS_API_TOKEN")


def write_to_file(filename: str, news: list):
    unique_id = uuid.uuid4()
    file_name = f"{filename}_{unique_id}.txt"

    with open(BASE_DIR.joinpath(file_name), "w") as f:
        for new in news:
            json.dump(new, f, sort_keys=True, indent=2)


def get_news(token: str, query: str):
    newsapi = NewsApiClient(api_key=token)
    # top_headlines = newsapi.get_top_headlines(
    #     # q="",
    #     category="technology",
    #     language="en",
    #     country="us",
    # )
    everything = newsapi.get_everything(
        q=query,
        language="en",
    )

    # /v2/top-headlines/sources
    # sources = newsapi.get_sources()

    json_str = json.dumps(everything)
    py_dict = json.loads(json_str)

    articles = py_dict["articles"]

    # print(len(py_dict["articles"]))

    write_to_file(query, articles)


def read_news():
    engine = pyttsx3.init()

    rate = engine.getProperty("rate")  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    engine.setProperty("rate", 125)  # setting up new voice rate

    engine.say("I will speak this text")

    engine.runAndWait()


# read_news()
get_news(token, "qgis")
