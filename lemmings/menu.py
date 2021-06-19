import pygame
import pygame_menu
import os
from settingsController import settings
import json

pygame.mixer.pre_init(44100,-16,1,512)

pygame.init()
surface = pygame.display.set_mode((800, 600))

s_click = pygame.mixer.Sound('Sounds/Sound_Click.wav')
pygame.mixer.music.load('Sounds/Main_Theme.mp3')
pygame.mixer.music.play(-1)


def set_difficulty(value, difficulty):
    s_click.play()
    pass


def start_the_game():
    s_click.play()
    os.startfile('main.py')
    pass


def settings():
    s_click.play()
    settings.getValue('Volume')

    pass


menu = pygame_menu.Menu(600,800, 'Lemmings the game',
                       theme=pygame_menu.themes.THEME_GREEN)


menu.add.label('Name:WeXLer')
menu.add.button('Play', start_the_game)
menu.add.button('Settings', settings)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.add.
menu.mainloop(surface)
