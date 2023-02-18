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
clock = pygame.time.Clock()


WIDTH = 800
HEIGHT = 500


def image_pre_process(relative_file_path=None, absolute_file_path=None):
    new_size = (96, 96)
    if relative_file_path:
        imageFile = Image.open(f"{BASE_DIR}/{relative_file_path}")
    if absolute_file_path:
        imageFile = Image.open(absolute_file_path)

    image = imageFile.resize(new_size, Image.Resampling.LANCZOS)

    # print(image)

    return ImageTk.PhotoImage(image)


# def get_music_detail(music_img=None, music_title=None, music_album=None):
def get_music_detail(music_path: str = None):
    music_img = image_pre_process(
        relative_file_path="images/apple-music-logo-circle-png-28.png"
    )
    music_title = "Music Title Not Found"
    music_album = "Album Title Not Found"
    if music_path:
        try:
            mp3 = stagger.read_tag(music_path)
            by_data = mp3[stagger.id3.APIC][0].data
            im = io.BytesIO(by_data)

            imageFile = Image.open(im)

            music_img = image_pre_process(absolute_file_path=im)
            music_title = mp3.artist
            music_album = mp3.album

        except:
            pass

    return music_title, music_album, music_img


def show_current_music(artist_name: tk.Frame, image_frame, music_path: str = None):
    # return get_music_detail(music_path)
    music_title, music_album, music_img = get_music_detail(music_path)

    # artist_name.config(text=music_title)
    # print(type(artist_name))


def add_to_playlist(listbox, filenames=None):
    if filenames:
        for filename in filenames:

            # listbox.insert(tk.END, filename + str(listbox.size() + 1))
            listbox.insert(tk.END, filename)


def open_file(listbox):
    f_types = [("MP3 Files", "*.mp3;*.wav;*.m4a;*.flac;*.mp4;*.wma;*.aac")]

    filenames = filedialog.askopenfilenames(filetypes=f_types)

    add_to_playlist(listbox, filenames)


def handle_play_btn(
    listbox: tk.Listbox,
    artist_name: tk.Frame,
    album_name: tk.Frame,
    music_logo: tk.Frame,
):
    # st = listbox.get(tk.ANCHOR)
    # all_list = listbox.get(0, tk.END)
    cur_index = listbox.curselection()[0]
    all_list = list(listbox.get(0, tk.END))
    # selected = listbox.select_set(cur_index, listbox.size())
    current_list = []
    # print(all_list)
    if listbox.size():
        # for i in listbox.curselection():
        for i in all_list:
            # while True:
            clock.tick(100)
            if cur_index == listbox.size():
                break

            cur_song = listbox.get(cur_index)
            if not pygame.mixer.music.get_busy():
                if not current_list:
                    current_list = all_list[:]
                    #     cur_song = current_list.pop(0)
                    cur_index += 1
                    cur_song = listbox.get(cur_index)

            # st = listbox.get(cur_index)

            music_title, music_album, music_img = get_music_detail(cur_song)
            artist_name.config(text=music_title)
            album_name.config(text=music_album)

            music_logo.configure(image=music_img)
            music_img.image = music_img

            pygame.mixer.music.load(cur_song)
            pygame.mixer.music.play()

        cur_index += 1


#


def handle_pause_btn():
    print("Clicked Pause")
