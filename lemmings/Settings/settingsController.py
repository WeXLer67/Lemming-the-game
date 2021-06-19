import json

class SettginsController(object):
    def __init__(self, filePath):
        self.filePath = filePath #Путь к файлу
        
    # Получить все настройки
    def getAllValue(self):
        settingsFile = open(self.filePath, 'r')
        fileContent = json.load(settingsFile)

        settingsFile.close()
        return fileContent

    # Получить значени по ключу
    def getValue(self, key):
        fileContent = self.getAllValue()

        return fileContent[key]

    # Установить значение по ключу
    def setValue(self, key, value):
        fileContent = self.getAllValue()
        fileContent[key] = value

        settingsFile = open(self.filePath, 'w')
        settingsFile.write(json.dumps(fileContent, indent = 4))
        settingsFile.close()

settings = SettginsController('./settings.json')