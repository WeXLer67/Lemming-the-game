from tkinter import *

def clicked():
    lbl.configure(text="Ну или работают немного ¯\_(ツ)_/¯")

def clicked_start():
    lbl.configure(text="Типо начал игру")

def clicked_settings():
    lbl.configure(text="Типо открылись настройки")

window = Tk()
window.title("Lemming the game")
window.geometry('800x600')

lbl = Label(window, text="Lemmings", font=("Arial Bold", 50), fg="black")
lbl.grid(column=0, row=0)

btn = Button(window, text="кнопки не работают", bg="black", fg="white", command=clicked)
btn_start = Button(window, text="кнопки не работают(Начать игру)", bg="black", fg="white", command=clicked_start)
btn_settings = Button(window, text="кнопки не работают(Настройки)", bg="black", fg="white", command=clicked_settings)
btn_exit = Button(window, text="Выход", bg="black", fg="white", command=window.destroy)
btn.grid(column=0, row=1)
btn_start.grid(column=0, row=2)
btn_settings.grid(column=0, row=3)
btn_exit.grid(column=0, row=4)

window.mainloop()