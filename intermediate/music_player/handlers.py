import pygame
import pathlib
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import stagger
import io
from PIL import Image, ImageTk

BASE_DIR = pathlib.Path(__file__).parent
pygame.mixer.init()


def image_pre_process(file_path):
    new_size = (96, 96)
    imageFile = Image.open(f"{BASE_DIR}/{file_path}")
    image = imageFile.resize(new_size, Image.Resampling.LANCZOS)

    return ImageTk.PhotoImage(image)


def get_music_detail(music_img=None, music_title=None, music_album=None):
    # mp3 = stagger.read_tag(BASE_DIR)
    # by_data = mp3[stagger.id3.APIC][0].data
    # im = io.BytesIO(by_data)
    # imageFile = Image.open(im)
    if music_img is None:
        music_img = image_pre_process("images/apple-music-logo-circle-png-28.png")
    if music_title is None:
        music_title = "Music Title Not Found"
    if music_album is None:
        music_album = "Album Title Not Found"

    return music_title, music_album, music_img


def show_current_music():
    return get_music_detail()


def add_to_playlist(listbox, filenames=None):
    if filenames:
        for filename in filenames:

            listbox.insert(tk.END, filename + str(listbox.size() + 1))


def open_file(listbox):
    f_types = [("MP3 Files", "*.mp3;*.wav;*.m4a;*.flac;*.mp4;*.wma;*.aac")]

    filenames = filedialog.askopenfilenames(filetypes=f_types)

    add_to_playlist(listbox, filenames)


def handle_play_btn():
    print(BASE_DIR)
    pygame.mixer.music.load(BASE_DIR)
    pygame.mixer.music.play(0)
    print("Clicked Play")


def handle_pause_btn():
    print("Clicked Pause")
