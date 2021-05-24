import pygame
import pygame_menu


pygame.init()
surface = pygame.display.set_mode((800, 800))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    if pygame.mouse.get_pressed():
        open('main (2).py')
    pass

def settings():

    pass

menu = pygame_menu.Menu(800,800, 'Lemmings the game',
                       theme=pygame_menu.themes.THEME_GREEN)

menu.add.label('Name:WeXLer')
menu.add.button('Play', start_the_game)
menu.add.button('Settings',settings)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)