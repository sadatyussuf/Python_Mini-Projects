import tkinter as tk
from tkinter import ttk
import pygame
import pathlib
import stagger
import io
from PIL import Image, ImageTk
from handlers import handle_pause_btn, handle_play_btn

WIDTH = 800
HEIGHT = 500

# BASE_DIR = pathlib.Path(__file__).parent / "music/foo.wav"
BASE_DIR = r"D:\Audio\Loyalty_Freak_Music_-_04_-_Cant_Stop_My_Feet_.mp3"


mp3 = stagger.read_tag(BASE_DIR)
by_data = mp3[stagger.id3.APIC][0].data
im = io.BytesIO(by_data)
imageFile = Image.open(im)

print(mp3.artist)
print(mp3.album)


window = tk.Tk()

window.title("Music Player")
window.configure(background="#262626")
window.geometry(f"{WIDTH}x{HEIGHT}")
# window.resizable(False, False)


# ---------------------------------------------------------------------------------
top_frame = tk.Frame(window, width=WIDTH, height=100, bg="#59004B")
top_frame.pack()

image_frame = tk.Frame(top_frame, width=100, height=100, bg="yellow")
image_frame.pack(side="left")

label_frame = tk.Frame(master=top_frame, bg="#59024B")
label_frame.pack()

artist_name = tk.Label(
    label_frame,
    text=f"{mp3.artist}",
    justify=["center"],
    font=("Helvetica", 30),
    bg="#59024B",
    fg="#E372F2",
)
album_name = tk.Label(
    label_frame,
    text=f"{mp3.album}",
    justify=["center"],
    font=("Helvetica", 15),
    bg="#59024B",
    fg="#E372F2",
)

artist_name.pack(ipady=5, ipadx=(WIDTH - 200) / 2)
album_name.pack(ipady=5, ipadx=(WIDTH - 200) / 2)


# # Resize the image
new_size = (96, 96)
image = imageFile.resize(new_size, Image.ANTIALIAS)

img = ImageTk.PhotoImage(image)
label = tk.Label(image_frame, image=img)
label.pack()
# ---------------------------------------------------------------------------------

# left_frame = tk.Frame(master=window, width=WIDTH / 2, height=HEIGHT - 100, bg="#E372F2")
# left_frame.pack(side="left")

# right_frame = tk.Frame(
#     master=window, width=WIDTH / 2, height=HEIGHT - 100, bg="#D90DA2"
# )
# right_frame.pack(side="right")


# p_frame = tk.Frame(master=window, width=250, height=250, bg="yellow")
# p_frame.grid(row=1, column=1)


# playlists_frame = tk.Frame(master=window, width=400, height=300, bg="green")
# playlists_frame.grid(row=1, column=5, padx=70)

# volumes_frame = tk.Frame(master=window, width=400, height=50, bg="blue")
# volumes_frame.grid(row=5, column=5)


# frame_btn = tk.Frame(master=window, width=WIDTH, bg="#000")

# play_btn = tk.Button(frame_btn, width=13, text="Play", command=handle_play_btn)
# play_btn.grid(row=0, column=0)

# pause_btn = tk.Button(frame_btn, width=13, text="Pause", command=handle_pause_btn)
# pause_btn.grid(row=0, column=1)

# stop_btn = tk.Button(frame_btn, width=13, text="Stop", command=handle_pause_btn)
# stop_btn.grid(row=0, column=2)

# resume_btn = tk.Button(frame_btn, width=13, text="Resume", command=handle_pause_btn)
# resume_btn.grid(row=0, column=3)

# prev_btn = tk.Button(frame_btn, width=13, text="Prev", command=handle_pause_btn)
# prev_btn.grid(row=0, column=4)

# next_btn = tk.Button(frame_btn, width=13, text="Next", command=handle_pause_btn)
# next_btn.grid(row=0, column=5)


# frame_btn.pack(fill=tk.BOTH, side=tk.BOTTOM)


window.mainloop()
