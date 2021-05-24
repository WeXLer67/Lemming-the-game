import os
from definitions import ROOT_DIR

# Функция для удобного импорта файлов
def getPathToFileFromFolder(filePath):
    return os.path.join(ROOT_DIR, filePath)