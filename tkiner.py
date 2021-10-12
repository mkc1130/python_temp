from tkinter import *

def process ():
    weight = float(e1.get())
    height = float(e2.get())
    bmi = round(weight / (height**2), 2)
    e3.insert(0, str(bmi))
    if (bmi < 18.5) :
        e4.insert(0, "저체중")
    elif(bmi < 24.9) :
        e4.insert(0, "표준")
    elif(bmi < 29.9) : 
        e4.insert(0, "과체중")
    elif(bmi < 30) :
        e4.insert(0, "비만")

window = Tk()
window.title("BMI 계산기")

l1 = Label(window, text="몸무게(kg)")
l2 = Label(window, text="키(M)")
l3 = Label(window, text="BMI")
l4 = Label(window, text="비만정도")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
l4.grid(row=3, column=0)

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e4 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

b1 = Button(window, text="BMI 계산!", command = process)
b1.grid(row=4, column=0)

window.mainloop()

    