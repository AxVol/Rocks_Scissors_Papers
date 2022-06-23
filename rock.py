import tkinter as tk 
from PIL import ImageTk
import random

running = True

def run():
    #Параметры окна
    root = tk.Tk()
    root.geometry("600x600")
    root.title("Камень, Ножницы, Бумага")
    root.resizable(height = False, width = False)
    root.iconphoto(True, tk.PhotoImage(file = ("graf/icon.png")))

    #Канвас с изображениями
    canvas = tk.Canvas(root, width = 600, height = 600)
    canvas.pack()

    background = ImageTk.PhotoImage(file = "graf/texture.png")
    canvas.create_image(100, 100, image = background)

    rockBot = ImageTk.PhotoImage(file = "graf/rock_bot.png")
    rock = ImageTk.PhotoImage(file = "graf/rock.png")
    canvas.create_image(140, 160, image = rock)

    scissorsBot = ImageTk.PhotoImage(file = "graf/scissors_bot.png")
    scissors = ImageTk.PhotoImage(file = "graf/scissors.png")
    canvas.create_image(150, 310, image = scissors)

    paperBot = ImageTk.PhotoImage(file = "graf/paper_bot.png")
    paper = ImageTk.PhotoImage(file = "graf/paper.png")
    canvas.create_image(140, 460, image = paper)

    canvas.create_text(300, 50, text = "Добро пожаловать в игру\nКамень, Ножницы, Бумага", 
                        font = "TimesNewRoman 21", fill = "orange")
    canvas.create_text(300, 120, text = "Выберите свой вариант...", 
                        font = "TimesNewRoman 14", fill = "white")

    #Выбор жеста врага
    def choice():
        global num
        Bot = [rockBot, scissorsBot, paperBot]
        num = random.randrange(0, 2)
        gesture = Bot[num]

        return gesture

    #Функция перезапуска
    def restart():
        root.destroy()

    #Оброботка клика
    out = []
    def result():
        canvas.delete("all")
        canvas.create_image(100, 100, image = background)

        #Кнопки перезапуска и выхода
        btnR = tk.Button(root, text = "Сыграть ещё раз", command = restart)
        btnR.configure(width = 20, height = 2, relief = tk.FLAT)
        canvas.create_window(140, 500, window = btnR)

        btnE = tk.Button(root, text = "Выход", command = exit)
        btnE.configure(width = 20, height = 2, relief = tk.FLAT)
        canvas.create_window(420, 500, window = btnE)

        #Выбор врага
        choiceBot = choice()
        canvas.create_image(440, 230, image = choiceBot)

        #Проверка выбора жеста
        if out[-1] == "0":
            canvas.create_image(140, 230, image = rockBot)
        elif out[-1] == "1":
            canvas.create_image(150, 230, image = scissorsBot)
        elif out[-1] == "2":
            canvas.create_image(140, 230, image = paperBot)

        #Проверка исхода победы/поражения
        if (out[-1] == str(num)):
            canvas.create_text(290, 50, text = "Ничья", font = "TimesNewRoman 30", fill = "orange")
        elif (((out[-1] == "0") and (num == 2)) or ((out[-1] == "1") and (num == 0)) or ((out[-1] == "2") and (num == 1))):
            canvas.create_text(290, 50, text = "Проигрыш = (", font = "TimesNewRoman 30", fill = "orange")
        elif (((out[-1] == "0") and (num == 1)) or ((out[-1] == "1") and (num == 2)) or ((out[-1] == "2") and (num == 0))):
            canvas.create_text(290, 50, text = "Выйгрыш = )", font = "TimesNewRoman 30", fill = "orange")


    #Кнопки
    def render_btn(x, y, text, width, height):
        btn = tk.Button(root, text = text, command = result)
        btn.configure(width = width, height = height, relief = tk.FLAT)
        canvas.create_window(x, y, window = btn)
        return btn

    btnr = render_btn(430, 200, "Камень", 20, 5)
    btnr.bind('<Button-1>', lambda x: out.append("0"))
    btns = render_btn(430, 350, "Ножницы", 20, 5)
    btns.bind('<Button-1>', lambda x: out.append("1"))
    btnp = render_btn(430, 500, "Бумага", 20, 5)
    btnp.bind('<Button-1>', lambda x: out.append("2"))

    #выход из игры
    def quit():
        global running

        running = False
        root.destroy()

    root.mainloop()

while running:
    run()