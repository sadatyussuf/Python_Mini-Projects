import pygame
import pathlib

BASE_DIR = pathlib.Path(__file__).parent / "music/foo.wav"
pygame.mixer.init()


def handle_play_btn():
    print(BASE_DIR)
    pygame.mixer.music.load(BASE_DIR)
    pygame.mixer.music.play(0)
    print("Clicked Play")


def handle_pause_btn():
    print("Clicked Pause")
