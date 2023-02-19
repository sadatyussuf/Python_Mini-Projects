import tkinter as tk


import pathlib
from PIL import Image, ImageTk
from handlers import (
    handle_pause_btn,
    handle_play_btn,
    open_file,
    handle_next_btn,
    handle_prev_btn,
)


WIDTH = 800
HEIGHT = 500

BASE_DIR = pathlib.Path(__file__).parent


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
top_frame = tk.Frame(window)
top_frame.pack()

image_frame = tk.Frame(top_frame)
image_frame.pack(side="left")

label_frame = tk.Frame(master=top_frame)
label_frame.pack()


artist_name = tk.Label(
    label_frame,
    text="Music Title Not Found",
    justify=["center"],
    font=("Helvetica", 30),
    bg="#205924",
    fg="#fff",
)
album_name = tk.Label(
    label_frame,
    text="Album Title Not Found",
    justify=["center"],
    font=("Helvetica", 15),
    bg="#205924",
    fg="#fff",
)

artist_name.pack(ipady=5, ipadx=(WIDTH - 200) / 2)
album_name.pack(ipady=5, ipadx=(WIDTH - 200) / 2)


photo = image_pre_process("images/apple-music-logo-circle-png-28.png")
music_logo = tk.Label(image_frame, image=photo)
music_logo.pack()

# * ---------------------------------------------------------------------------------


right_frame = tk.Frame(master=window, bg="#3CA643")
right_frame.pack(side="right")

select_music_btn = tk.Button(
    master=right_frame,
    text="Add Music",
    bg="#0D0D0D",
    fg="#41F24D",
    command=lambda: open_file(listbox),
)
select_music_btn.pack(side=["top"], padx=10, pady=5, anchor=tk.W)

playlists_frame = tk.Frame(master=right_frame)
playlists_frame.pack(side=["bottom"], padx=10, pady=5)
# !------------------------------------------------------

listbox = tk.Listbox(
    master=playlists_frame,
    height=22,
    width=int(((WIDTH / 2) / 7)),
    bg="#0D0D0D",
    fg="#41F24D",
)

listbox.pack(side="left", fill=tk.BOTH, expand=True)

# *------------------------------------------------------------

left_frame = tk.Frame(master=window, bg="#205924")
left_frame.pack(side="left")

first_left_frame = tk.Frame(master=left_frame, bg="#41F24D")
first_left_frame.pack()


img = image_pre_process("images/play-button.png")
play_btn = tk.Button(
    first_left_frame,
    width=100,
    height=100,
    bg="#41F24D",
    image=img,
    border=0,
    command=lambda: handle_play_btn(listbox, artist_name, album_name, music_logo),
)
play_btn.pack(pady=26)


second_left_frame = tk.Frame(master=left_frame, bg="#41F24D")
second_left_frame.pack()
img2 = image_pre_process("images/next-button.png")
next_btn = tk.Button(
    second_left_frame,
    width=100,
    height=100,
    bg="#41F24D",
    image=img2,
    border=0,
    command=lambda: handle_next_btn(listbox, artist_name, album_name, music_logo),
)
next_btn.pack(side=tk.RIGHT, padx=50)

img3 = image_pre_process("images/back-button.png")
prev_btn = tk.Button(
    second_left_frame,
    width=100,
    height=100,
    bg="#41F24D",
    image=img3,
    border=0,
    command=lambda: handle_prev_btn(listbox, artist_name, album_name, music_logo),
)
prev_btn.pack(side=tk.LEFT, padx=65)


third_left_frame = tk.Frame(master=left_frame, bg="#41F24D")
third_left_frame.pack()

img4 = image_pre_process("images/pause.png")
pause_btn = tk.Button(
    third_left_frame,
    width=100,
    height=100,
    bg="#41F24D",
    image=img4,
    border=0,
    command=handle_pause_btn,
)
pause_btn.pack(side=tk.RIGHT, pady=26)


window.mainloop()
