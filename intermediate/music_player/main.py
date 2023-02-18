import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile

import pygame
import pathlib
import stagger
import io
from PIL import Image, ImageTk
from handlers import (
    handle_pause_btn,
    handle_play_btn,
    open_file,
    add_to_playlist,
    show_current_music,
)


WIDTH = 800
HEIGHT = 500

BASE_DIR = pathlib.Path(__file__).parent
# print(BASE_DIR)
# # BASE_DIRs = r"D:\Audio\Loyalty_Freak_Music_-_04_-_Cant_Stop_My_Feet_.mp3"
# BASE_DIRs = r"D:\Audio\test.wav"

# try:
#     mp3 = stagger.read_tag(BASE_DIRs)
#     print(mp3)
# except:
#     pass

# by_data = mp3[stagger.id3.APIC][0].data
# im = io.BytesIO(by_data)
# imageFile = Image.open(im)

# print(mp3.artist)
# print(mp3.album)


window = tk.Tk()

window.title("Music Player")
window.configure(background="#262626")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False, False)


def image_pre_process(file_path):
    new_size = (96, 96)
    imageFile = Image.open(f"{BASE_DIR}/{file_path}")
    image = imageFile.resize(new_size, Image.Resampling.LANCZOS)

    return ImageTk.PhotoImage(image)


# ---------------------------------------------------------------------------------
top_frame = tk.Frame(window, width=WIDTH, height=100, bg="#59004B")
top_frame.pack()

image_frame = tk.Frame(top_frame, width=100, height=100, bg="yellow")
image_frame.pack(side="left")

label_frame = tk.Frame(master=top_frame, bg="#59024B")
label_frame.pack()


artist_name = tk.Label(
    label_frame,
    text="Music Title Not Found",
    justify=["center"],
    font=("Helvetica", 30),
    bg="#59024B",
    fg="#E372F2",
)
album_name = tk.Label(
    label_frame,
    text="Album Title Not Found",
    justify=["center"],
    font=("Helvetica", 15),
    bg="#59024B",
    fg="#E372F2",
)

artist_name.pack(ipady=5, ipadx=(WIDTH - 200) / 2)
album_name.pack(ipady=5, ipadx=(WIDTH - 200) / 2)


# img = ImageTk.PhotoImage(image)
# label = tk.Label(image_frame, image=img)
photo = image_pre_process("images/apple-music-logo-circle-png-28.png")
music_logo = tk.Label(image_frame, image=photo)
music_logo.pack()
# * ---------------------------------------------------------------------------------

right_frame = tk.Frame(
    master=window, width=WIDTH / 2, height=HEIGHT - 100, bg="#D90DA2"
)
right_frame.pack(side="right")

select_music_btn = tk.Button(
    master=right_frame,
    text="Add Music",
    bg="#59004B",
    fg="#E372F3",
    command=lambda: open_file(listbox),
)
select_music_btn.pack(side=["top"], padx=10, pady=5, anchor=tk.W)

playlists_frame = tk.Frame(
    master=right_frame, width=(WIDTH - 100) / 2, height=HEIGHT - 200, bg="green"
)
playlists_frame.pack(side=["bottom"], padx=10, pady=5)
# !------------------------------------------------------

listbox = tk.Listbox(
    master=playlists_frame,
    height=22,
    width=int(((WIDTH / 2) / 7)),
)

listbox.pack(side="left", fill=tk.BOTH, expand=True)

# *------------------------------------------------------------

left_frame = tk.Frame(master=window, width=WIDTH / 2, height=HEIGHT - 100, bg="#E372F2")
left_frame.pack(side="left")

first_left_frame = tk.Frame(
    master=left_frame, width=WIDTH / 2, height=(HEIGHT - 100) / 4, bg="red"
)
first_left_frame.pack()


img = image_pre_process("images/375.png")
play_btn = tk.Button(
    first_left_frame,
    width=100,
    height=100,
    bg="#E372F2",
    image=img,
    border=0,
    command=lambda: handle_play_btn(listbox, artist_name, album_name, music_logo),
)
play_btn.pack()


# second_left_frame = tk.Frame(
#     master=left_frame, width=WIDTH / 2, height=(HEIGHT - 100) / 4, bg="yellow"
# )
# second_left_frame.pack()
# img2 = image_pre_process("images/4871417.png")
# next_btn = tk.Button(
#     second_left_frame,
#     width=100,
#     height=100,
#     bg="yellow",
#     image=img2,
#     border=0,
#     # command=handle_next_btn,
# )
# next_btn.pack(side=tk.LEFT, padx=50)

# img3 = image_pre_process("images/2514.png")
# prev_btn = tk.Button(
#     second_left_frame,
#     width=100,
#     height=100,
#     bg="yellow",
#     image=img3,
#     border=0,
#     # command=handle_prev_btn,
# )
# prev_btn.pack(side=tk.RIGHT, padx=50)


# third_left_frame = tk.Frame(
#     master=left_frame, width=WIDTH / 2, height=(HEIGHT - 100) / 4, bg="black"
# )
# third_left_frame.pack()
# img4 = image_pre_process("images/2514.png")
# pause_btn = tk.Button(
#     third_left_frame,
#     width=100,
#     height=100,
#     bg="yellow",
#     image=img4,
#     border=0,
#     # command=handle_pause_btn,
# )
# pause_btn.pack(
#     side=tk.RIGHT,
# )

# fourth_left_frame = tk.Frame(
#     master=left_frame, width=WIDTH / 2, height=(HEIGHT - 100) / 4, bg="green"
# )
# fourth_left_frame.pack()


window.mainloop()
