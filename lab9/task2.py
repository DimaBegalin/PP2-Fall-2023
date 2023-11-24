import pygame
import os
from pygame.locals import *

# p - play
# s - stop
# n - next
# l - previous

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music Player")
WHITE = (255, 255, 255)

music_directory = "./tracks"
music_files = [f for f in os.listdir(music_directory) if f.endswith('.mp3')]

pygame.mixer.init()

current_song_index = 0
current_song = os.path.join(music_directory, music_files[current_song_index])
pygame.mixer.music.load(current_song)

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(music_files)
    load_and_play_current_song()

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(music_files)
    load_and_play_current_song()

def load_and_play_current_song():
    global current_song
    current_song = os.path.join(music_directory, music_files[current_song_index])
    pygame.mixer.music.load(current_song)
    play_music()

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        elif event.type == KEYDOWN:
            if event.key == K_p:
                play_music()

            elif event.key == K_s:
                stop_music()

            elif event.key == K_n:
                next_song()

            elif event.key == K_l:
                previous_song()

    pygame.display.flip()
