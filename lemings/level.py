import pygame
from definitions import BACKGROUND_COLOUR

# Класс уровня
class Level():
    # Принимает как аргумент путь к картинки уровня
    def __init__(self, imagePath):
        self.screen = pygame.display.get_surface() # Создание дисплея
        self.background = pygame.Surface(self.screen.get_size()).convert() # Создание полотна на котором будет располагаться картинка
        self.charImage = pygame.image.load(imagePath).convert() # Загрузка изображения
        self.background.blit(self.charImage, (0, 0)) # Добавление изображение на полотно
        
    def draw(self):
        # Отрисовка изображения в цикле
        self.screen.blit(self.background, (0, 0))

        # Рисование по картинке
        # Зажатая левая мышка
        if pygame.mouse.get_pressed()[0]:
            # Тут надо в доке глянуть какие аргументы за что отвечают
            pygame.draw.rect(self.background, (255, 0, 0), (pygame.mouse.get_pos()[0] - 5, pygame.mouse.get_pos()[1] - 5, 10, 10))
        
        # Зажатая правая мышка
        if pygame.mouse.get_pressed()[2]:
            # Тут надо в доке глянуть какие аргументы за что отвечают
            pygame.draw.rect(self.background, BACKGROUND_COLOUR, (pygame.mouse.get_pos()[0] - 5, pygame.mouse.get_pos()[1] - 5, 10, 10))
