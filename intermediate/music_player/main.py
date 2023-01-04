import tkinter as tk
import pygame
import pathlib

WIDTH = 600
HEIGHT = 500

BASE_DIR = pathlib.Path(__file__).parent / "music/foo.wav"
pygame.mixer.init()


def handle_play_btn():
    print(BASE_DIR)
    pygame.mixer.music.load(BASE_DIR)
    pygame.mixer.music.play(0)
    print("Clicked Play")


def handle_pause_btn():
    print("Clicked Play")


window = tk.Tk()

window.title("Music Player")
window.configure(background="#000")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False, False)

frame_track_list = tk.Frame(
    master=window, width=WIDTH / 2, height=HEIGHT / 5, bg="#d0f0e0"
)
frame_track_list.pack()
# frame_btn.pack(fill=tk.BOTH, side=tk.BOTTOM)


frame_btn = tk.Frame(master=window, width=WIDTH, bg="#000")

play_btn = tk.Button(frame_btn, width=13, text="Play", command=handle_play_btn)
play_btn.grid(row=0, column=0)

pause_btn = tk.Button(frame_btn, width=13, text="Pause", command=handle_pause_btn)
pause_btn.grid(row=0, column=1)

stop_btn = tk.Button(frame_btn, width=13, text="Stop", command=handle_pause_btn)
stop_btn.grid(row=0, column=2)

resume_btn = tk.Button(frame_btn, width=13, text="Resume", command=handle_pause_btn)
resume_btn.grid(row=0, column=3)

prev_btn = tk.Button(frame_btn, width=13, text="Prev", command=handle_pause_btn)
prev_btn.grid(row=0, column=4)

next_btn = tk.Button(frame_btn, width=13, text="Next", command=handle_pause_btn)
next_btn.grid(row=0, column=5)


frame_btn.pack(fill=tk.BOTH, side=tk.BOTTOM)


window.mainloop()
