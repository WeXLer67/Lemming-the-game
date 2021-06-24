import pygame
from definitions import BACKGROUND_COLOUR
from utils.getPathToFileFromFolder import getPathToFileFromFolder


pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
s_death = pygame.mixer.Sound(getPathToFileFromFolder('./Sounds/Sound_Death.wav'))
block = pygame.mixer.Sound(getPathToFileFromFolder('./Sounds/Block.wav'))

class Lemming(pygame.sprite.Sprite): # Наследование класс Lemming от класса pygame.sprite.Sprite
    def __init__(self, start_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(getPathToFileFromFolder('images/lemming.png')).convert() # Загрузка изображения
        self.rect = self.image.get_rect()
        self.rect.center = start_position # Начальная позиция
        self.direction = 1 # Направление движения
        self.climbheight = 4 # Высота на которую можно подняться
        self.isDead = False # Флаг смерти
        self.deadLine = 60 # Максимально возможная высота падения
        self.startFallenPoint = None # Точка с которой началось падение
        self.fallenSpeed = 1 # Скорость падения

    # Функция определяет пиксель по позиции
    def groundatposition(self, pos):

        display_size = pygame.display.get_window_size()

        if pos[0] >= display_size[0] or pos[1] >= display_size[1]:
            return True

        if pos[0] <= 0 or pos[1] <= 0:
            return True

        # Получене пикселя по позиции
        pixel = pygame.display.get_surface().get_at(pos)

        if pixel != BACKGROUND_COLOUR:
            return True
        else:
            return False

    def update(self):
        if self.isDead:
            return

        # Проверяем если под персонажем нет земли, переводим в состояние падения
        if not self.groundatposition(pos = self.rect.bottomleft) and not self.groundatposition(pos = self.rect.bottomright):

            # Запоминаем точку с которой началось падение
            if self.startFallenPoint is None:
                self.startFallenPoint = self.rect.bottom

            # Увеличиваем y для того, что бы персонаж падал
            self.rect.y += self.fallenSpeed

        # Если под ногами есть земля, заставляем персонажа двигаться
        else:
            # Смерть если при приземлении если преодолел больше дозволенной дистанции
            if self.startFallenPoint is not None and abs(self.startFallenPoint - self.rect.bottom) >= self.deadLine:
                self.isDead = True
                s_death.play()
                return

            # Если персонаж не умер, сбрасываем координату которую мы запомнили
            self.startFallenPoint = None

            height = 0

            found = False

            while (found == False) and (height <= self.climbheight):

                # Если направление движение вправо
                if self.direction == 1:
                    # Брать пиксели справа - self.rect.right и сверху с учетом высоты персонажа.
                    positioninfront = (self.rect.right, self.rect.top + (self.rect.height - 1) - height)
                else:
                    # Брать пиксели слева - self.rect.left и сверху с учетом высоты персонажа.
                    positioninfront = (self.rect.left, self.rect.top + (self.rect.height - 1) - height)

                # Если справа от персонажа не стена, двигаемся в право
                if not self.groundatposition(pos = positioninfront):
                    self.rect.x += self.direction

                    # Пытаемся взобраться на уступ если он есть
                    self.rect.y -= height
                    found = True

                # После попытки взобраться на уступ опускаемся вниз, что бы не было видно как персонаж немного подергивается во время попыток взобраться
                height += 1

            # Если столкнулся со стеной, изменить направление движения
            if not found:
                self.direction *= -1
                block.play()
                # print('поражение')
