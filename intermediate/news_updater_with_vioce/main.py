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

    def formatting_text(new):
        title, author = new["title"], ["newauthor"]
        url, urlToImage = new["url"], new["urlToImage"]
        source_name, publishedAt = new["source"]["name"], new["publishedAt"]
        content, description = new["content"], new["description"]

        format_str = f"\n ---------- Author = {author} ---------- Source = {source_name} ---------- \n \n {'':^10} {title.upper()} \n \n {content} \n \n {description.lower()} \n \n URL = {url} \n UrlToImage = {urlToImage}  \n \n ---------- ---------- Date Published = {publishedAt} ---------- ---------- \n \n \n \n"

        return format_str

    news = list(map(formatting_text, news))
    with open(BASE_DIR.joinpath(file_name), "w") as f:
        for new in news:
            f.write(new)


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

    json_str = json.dumps(everything)
    py_dict = json.loads(json_str)

    articles = py_dict["articles"]

    write_to_file(query, articles)


def read_news():
    engine = pyttsx3.init()
    # getting details of current speaking rate
    rate = engine.getProperty("rate")
    print(rate)  # printing current voice rate
    engine.setProperty("rate", 125)  # setting up new voice rate

    engine.say("I will speak this text")

    engine.runAndWait()


# read_news()
get_news(token, "qgis")
