import pygame
import datetime
from lemming import Lemming
from level import Level
from utils.getPathToFileFromFolder import getPathToFileFromFolder

# Размеры окна
HEIGHT = 800
WIDTH = 800

# Ограничение по FPS
FPS = 60


pygame.init() # Инит игры
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создание окна
pygame.display.set_caption("My Game") # Заголовок для окна
clock = pygame.time.Clock() # Создание часов для ограничение FPS

max_lemmings = 10 # Максимальное число персонажей
start_position = (100, 200) # Начальная позиция персонажей
lemmings = pygame.sprite.Group() # Создание группы для персонажей

player = Lemming(start_position) # Инит персонажа
lemmings.add(player) # Добавление персонажа в группу

# Создание уровня
level = Level(getPathToFileFromFolder('./images/level.png'))

now = datetime.datetime.now()

# Цикл игры
running = True
while running:

    # Держим цикл на правильной скорости
    clock.tick(FPS)



    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            lemmings.add(player)
            print(1)

    # Отрисовка карты
    level.draw()

    # Вызов функции которая просчитывает движение
    lemmings.update()

    # Отрисовка лемингов
    lemmings.draw(level.screen)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


pygame.quit()