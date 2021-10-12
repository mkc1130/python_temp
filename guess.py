from tkinter import *
import random

answer = random.randint(1, 100)
limit = 10
global limited
limited = random.randint(0,0) + 10

def guessing() : 
    guess = int (guessField.get())
    if limit > 0 :
        if guess > answer :
            msg = "정답보다 높음!"
        elif guess < answer :
            msg = "정답보다 낮음!"
        else :
            msg = "정답입니다!"
    
        resultLabel["text"] = msg
        guessField.delete(0, 5)

def reset() : 
    global answer
    answer = random.randint(1, 100)
    resultLabel["text"] = "다시 한번 하세요!"

window = Tk()
window.title("숫자 예측 게임")
window.configure(bg="white")
window.geometry("500x80")

titleLabel = Label(window, text = "숫자 게임에 오신 것을 환영합니다!", bg = "white")
titleLabel.pack()

guessField = Entry(window)
guessField.pack(side="left")
trybutton = Button(window, text = "시도", fg = "green", bg = "white", command = guessing)
trybutton.pack(side = "left")

resetButton = Button(window, text = "초기화", fg = "red", bg = "white", command = reset)
resetButton.pack(side = "left")
resultLabel = Label(window, text = "1부터 100사이의 숫자를 입력하시오.", bg = "white")
resultLabel.pack(side = "left")

limitedLabel = Label(window, text = "", fg = "magenta", bg = "white")
limitedLabel.pack()

window.mainloop()


