from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from settingsController import settings
from utils.getPathToFileFromFolder import getPathToFileFromFolder
import pygame



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 563)
        f = settings.getValue('Volume')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(getPathToFileFromFolder('./images/img_icon.ico')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-6, -1, 821, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.Main_Menu = QtWidgets.QWidget()
        self.Main_Menu.setObjectName("Main_Menu")
        self.img = QtWidgets.QLabel(self.Main_Menu)
        self.img.setGeometry(QtCore.QRect(-50, -10, 861, 561))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap(getPathToFileFromFolder('./images/img_menu.jpg')))
        self.img.setObjectName("img")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Main_Menu)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(200, 120, 351, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.Btn_Play = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Btn_Play.setFont(font)
        self.Btn_Play.setObjectName("Btn_Play")
        self.verticalLayout_2.addWidget(self.Btn_Play)
        self.Btn_Help = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Btn_Help.setFont(font)
        self.Btn_Help.setObjectName("Btn_Help")
        self.verticalLayout_2.addWidget(self.Btn_Help)
        self.Btn_Exit = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Btn_Exit.setFont(font)
        self.Btn_Exit.setObjectName("Btn_Exit")
        self.verticalLayout_2.addWidget(self.Btn_Exit)
        self.tabWidget.addTab(self.Main_Menu, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.img2 = QtWidgets.QLabel(self.Settings)
        self.img2.setGeometry(QtCore.QRect(-50, -10, 861, 561))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.img2.setFont(font)
        self.img2.setText("")
        self.img2.setPixmap(QtGui.QPixmap(getPathToFileFromFolder('./images/img_menu.jpg')))
        self.img2.setObjectName("img2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Settings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 120, 351, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.Slider_Volume = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.Slider_Volume.setMouseTracking(False)
        self.Slider_Volume.setTabletTracking(False)
        self.Slider_Volume.setAcceptDrops(False)
        self.Slider_Volume.setAutoFillBackground(True)
        self.Slider_Volume.setMaximum(100)
        self.Slider_Volume.setSingleStep(1)
        self.Slider_Volume.setProperty("value", f)
        self.Slider_Volume.setValue(f)
        self.Slider_Volume.setSliderPosition(f)
        self.Slider_Volume.setTracking(True)
        self.Slider_Volume.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Volume.setInvertedAppearance(False)
        self.Slider_Volume.setInvertedControls(False)
        self.Slider_Volume.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider_Volume.setObjectName("Slider_Volume")
        self.verticalLayout.addWidget(self.Slider_Volume)
        self.Btn_Accept = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Btn_Accept.setFont(font)
        self.Btn_Accept.setObjectName("Btn_Accept")
        self.verticalLayout.addWidget(self.Btn_Accept)
        self.tabWidget.addTab(self.Settings, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.Btn_Exit.clicked.connect(MainWindow.close)
        self.Btn_Help.clicked.connect(MainWindow.hide)
        self.Btn_Help.clicked.connect(self.get_help)
        self.Btn_Help.clicked.connect(MainWindow.show)
        self.Btn_Play.clicked.connect(MainWindow.hide)
        self.Btn_Play.clicked.connect(self.game)
        self.Btn_Play.clicked.connect(MainWindow.show)
        self.Btn_Accept.clicked.connect(self.change_value)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lemmings"))
        self.label_4.setText(_translate("MainWindow", "Lemmings"))
        self.Btn_Play.setText(_translate("MainWindow", "Играть"))
        self.Btn_Help.setText(_translate("MainWindow", "Как играть"))
        self.Btn_Exit.setText(_translate("MainWindow", "Выйти"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main_Menu), _translate("MainWindow", "Главное меню"))
        self.label_3.setText(_translate("MainWindow", "Громкость"))
        self.Btn_Accept.setText(_translate("MainWindow", "Применить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Настройки звука"))

    def get_help(self):
        os.system('Help.docx')

    def change_value(self):
        settings.setValue('Volume', self.Slider_Volume.value())
        print(settings.getValue('Volume'))


    def game(self):
        import pygame
        from lemming import Lemming
        from level import Level
        # from final import Final

        # Размеры окна
        HEIGHT = 800
        WIDTH = 800

        # Ограничение по FPS
        FPS = 60

        pygame.init()  # Инит игры
        screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна
        pygame.display.set_caption("My Game")  # Заголовок для окна
        clock = pygame.time.Clock()  # Создание часов для ограничение FPS

        start_position = (100, 200)  # Начальная позиция персонажей
        lemmings = pygame.sprite.Group()  # Создание группы для персонажей
        player = Lemming(start_position)  # Инит персонажа
        lemmings.add(player)  # Добавление персонажа в группу
        # finals = Final(WIDTH,HEIGHT)

        # Создание уровня
        level = Level(getPathToFileFromFolder('./images/level.png'))

        final = pygame.image.load(getPathToFileFromFolder('./images/final1.png')).convert_alpha()
        f_rect = final.get_rect(centerx = WIDTH // 2, bottom = HEIGHT - 40)

        def collide():
            if f_rect.collidepoint(player.rect.center):
                print('победа')

        pygame.mixer.music.load(getPathToFileFromFolder('./Sounds/menu_music.mp3'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(settings.getValue('Volume')/100)

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

            collide()

            # Отрисовка карты
            level.draw()

            screen.blit(final, f_rect)

            # Вызов функции которая просчитывает движение
            lemmings.update()

            # Отрисовка лемингов
            lemmings.draw(level.screen)


            # После отрисовки всего, переворачиваем экран
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
