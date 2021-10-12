import tkinter as tk
from tkinter.constants import INSERT, NONE, RAISED, RIGHT
 
root = tk.Tk()
root.title("Tkinter Calculator")
root.geometry("400x625")
root.configure(background= 'gainsboro')

upper_frame = tk.Frame(root, width=400, height=70, bg = 'white')
upper_frame.pack(pady=40)
 
down_frame = tk.Frame(root, width=400, height=100, bg = 'gainsboro')
down_frame.pack(padx=10, pady=10)
 
entry = tk.Entry(upper_frame,font=("Courier",30),relief=RAISED, justify=RIGHT)
entry.pack(side = "bottom",ipady=30)
entry.insert(0,"")

global f_num
 
def button_clicked(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))
 
def button_clear():
    f_num = ''
    entry.delete(0, tk.END)
 
def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    entry.delete(0, tk.END)
 
def button_sub():
    first_number = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    entry.delete(0, tk.END)
 
def button_mul():
    first_number = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    entry.delete(0, tk.END)
 
def button_div():
    first_number = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_mod():
    first_number = entry.get()
    global f_num
    global math
    math = 'mod'
    f_num = int(first_number)
    entry.delete(0, tk.END)
 
def button_equal():
    global s_num
    entry.delete(0, tk.END)
    while(f_num != 0) :
        if math == 'addition':
            entry.insert(0,"%.2f",float(f_num + s_num))
            break
 
        if math == 'subtraction':
            entry.insert(0,"%.2f",float(f_num - s_num))
            break
 
        if math == 'multiplication':
            entry.insert(0,"%.2f",float(f_num * s_num))
            break
 
        if math == 'division':
            entry.insert(0,"%.2f",float(f_num / s_num))
            break

        if math == 'mod':
            entry.insert(0,"%.2f",float(f_num % s_num))
            break
        

def button_delete():
    number = entry.delete(len(entry.get())-1,"end")

def button_clear_entry():
    global f_num
    f_num = 0;
    entry.delete(0, tk.END)

def button_fra():
    first_number = int(entry.get())
    global f_num
    f_num = 1 / first_number
    entry.delete(0, tk.END)
    entry.insert(INSERT, f_num)
    #global temp
    #temp = "1/"+str(first_number)
    #entry.insert(INSERT, temp)


 
 
btn7 = tk.Button(down_frame,text='7', padx=15, pady=10, font=("Courier",15,"bold"),width=4, height=1,command=lambda: button_clicked(7), bg = 'white')
btn7.grid(column=0, row=2, padx=5, pady=5)
btn8 = tk.Button(down_frame,text='8', padx=15, pady=10, font=("Courier",15,"bold"),width=4, height=1,command=lambda: button_clicked(8), bg = 'white')
btn8.grid(column=1, row=2, padx=5, pady=5)
btn9 = tk.Button(down_frame,text='9', padx=15, pady=10, font=("Courier",15,"bold"),width=4, height=1,command=lambda: button_clicked(9), bg = 'white')
btn9.grid(column=2, row=2, padx=5, pady=5)
 
btn4 = tk.Button(down_frame,text='4', padx=15, pady=10, font=("Courier",15,"bold"),width=4, height=1,command=lambda: button_clicked(4), bg = 'white')
btn4.grid(column=0, row=3, padx=5, pady=5)
btn5 = tk.Button(down_frame,text='5', padx=15, pady=10, font=("Courier",15,"bold"),width=4, height=1,command=lambda: button_clicked(5), bg = 'white')
btn5.grid(column=1, row=3, padx=5, pady=5)
btn6 = tk.Button(down_frame,text='6', padx=15, pady=10, font=("Courier",15,"bold"),width=4, height=1,command=lambda: button_clicked(6), bg = 'white')
btn6.grid(column=2, row=3, padx=5, pady=5)
 
btn1 = tk.Button(down_frame,text='1', padx=15, pady=10, font=("Courier",15,"bold"),width=4, height=1,command=lambda: button_clicked(1), bg = 'white')
btn1.grid(column=0, row=4, padx=5, pady=5)
btn2 = tk.Button(down_frame,text='2', padx=15, pady=10, font=("Courier",15,"bold"),width=4, height=1,command=lambda: button_clicked(2), bg = 'white')
btn2.grid(column=1, row=4, padx=5, pady=5)
btn3 = tk.Button(down_frame,text='3', padx=15, pady=10, font=("Courier",15,"bold"),width=4, height=1,command=lambda: button_clicked(3), bg = 'white')
btn3.grid(column=2, row=4, padx=5, pady=5)
 
btn_pm = tk.Button(down_frame,text='+/-', padx=5, pady=10, font=("times",15),width=6, height=1,command=lambda: button_clicked('-'), bg = 'white')
btn_pm.grid(column=0, row=5, padx=5, pady=5)
btn0 = tk.Button(down_frame,text='0', padx=15, pady=10, font=("Courier",15,"bold"),width=4, height=1,command=lambda: button_clicked(0), bg = 'white')
btn0.grid(column=1, row=5, padx=5, pady=5)
btn_p = tk.Button(down_frame,text='.', padx=15, pady=10, font=("Courier",15,"bold"),width=4, height=1,command=lambda: button_clicked('.'), bg = 'white')
btn_p.grid(column=2, row=5, padx=5, pady=5)
 
btn_mul = tk.Button(down_frame,text='X', padx=15, pady=10, font=("times",15),width=4, height=1,command=button_mul)
btn_mul.grid(column=3, row=2, padx=5, pady=5)
btn_sub = tk.Button(down_frame,text='-', padx=15, pady=10, font=("times",15),width=4, height=1,command=button_sub)
btn_sub.grid(column=3, row=3, padx=5, pady=5)
btn_add = tk.Button(down_frame, text='+', padx=15, pady=10, font=("times",15),width=4, height=1,command=button_add)
btn_add.grid(column=3, row=4, padx=5, pady=5)
btn_div = tk.Button(down_frame, text='/', padx=15, pady=10, font=("times",15),width=4, height=1,command=button_div)
btn_div.grid(column=3, row=1, padx=5, pady=5)
btn_fra = tk.Button(down_frame, text='1/x', padx=15, pady=10, font=("times",15),width=4, height=1,command=button_fra)
btn_fra.grid(column=0, row=1, padx=5, pady=5)

btn_mod = tk.Button(down_frame, text='%', padx=15, pady=10, font=("times",15),width=4, height=1,command=button_mod)
btn_mod.grid(column=0, row=0, padx=5, pady=5)
btn_ce = tk.Button(down_frame, text='CE', padx=15, pady=10, font=("times",15),width=4, height=1,command=button_clear_entry)
btn_ce.grid(column=1, row=0, padx=5, pady=5)
btn_c = tk.Button(down_frame, text='C', padx=15, pady=10, font=("times",15),width=4, height=1,command=button_clear)
btn_c.grid(column=2, row=0, padx=5, pady=5)
btn_delete = tk.Button(down_frame, text='☒', padx=15, pady=10, font=("times",15),width=4, height=1,command=button_delete)
btn_delete.grid(column=3, row=0, padx=5, pady=5)
 
btn_res = tk.Button(down_frame, text='=', padx=15, pady=10, font=("times",15),width=4, height=1,command=button_equal, bg = 'cornflowerblue')
btn_res.grid(column=3, row=5, padx=5, pady=5)
 
btn3 = tk.Button(root,text='9')
 
root.mainloop()