import json
import os
import uuid
import wave
from pathlib import Path

import pyaudio
import pyttsx3
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()
BASE_DIR = Path(__file__).parent

token = os.environ.get("NEWS_API_TOKEN")


def write_to_file(filename: str, news: list):
    unique_id = uuid.uuid4()
    file_name = f"{filename}_{unique_id}.txt"
    # file_name = f"{filename}.txt"

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

    return file_name


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

    articles = py_dict["articles"][4:6]

    return write_to_file(query, articles)


def read_news(get_filez=None):
    get_file = list(BASE_DIR.glob("*.txt"))[0]

    engine = pyttsx3.init()

    with open(get_file, "r") as f:
        text = f.read()

    engine.setProperty("rate", 150)  # setting up new voice rate
    engine.setProperty("volume", 0.9)  # setting up new voice volume

    # Say the text out loud
    engine.say(text)
    engine.runAndWait()


def record_name():
    # Initialize the pyaudio recording parameters
    audio = pyaudio.PyAudio()
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5

    # Start recording
    stream = audio.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )
    print("Recording started...")
    frames = []
    for _ in range(int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Recording finished.")

    # Stop the stream and terminate the pyaudio object
    stream.stop_stream()
    stream.close()
    audio.terminate()

    filename = "results.wav"

    # Save the recorded audio to a file
    with wave.open(BASE_DIR.joinpath(filename), "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        # wf.writeframes(b"".join(frames))

    # wf = wave.open(BASE_DIR.joinpath(filename), "wb")
    # wf.setnchannels(CHANNELS)
    # wf.setsampwidth(audio.get_sample_size(FORMAT))
    # wf.setframerate(RATE)
    # wf.writeframes(b"".join(frames))
    # wf.close()

    print(f"Recording saved to {filename}.")


def main():
    de_file = get_news(token, "qgis")
    read_news(de_file)
    record_name()


if __name__ == "__main__":
    main()
