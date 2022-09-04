##This creates the Mp3 playlist##

import os
import pygame

pygame.init()
pygame.mixer.init()

path = 'D:\\Users\Imeah\Music'
lists_of_songs = os.listdir(path)


def play_music():
    for song in lists_of_songs:
        if song.endswith(".mp3"):
            file_path = path + song
            pygame.mixer.music.load(str(file_path))
            pygame.mixer.music.play()
            print("Playing: ")
            print("Playing:: ")
            print("Playing::: ")
            print("Playing:::: ")
            print("Playing::::: " + song)
            while pygame.mixer.music.get_busy():
                continue


def add_to_playlist():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
