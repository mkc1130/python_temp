from tkinter import *
id_list = ['강민서','권병욱','김동윤', '김상경', '김유성', '김장환', '박정현', '송태양', '신민성', '심승현', '안종두', '이건호', '이한울', '정다운', '조현규', '허진웅', '황선빈',]
password_list = ['2101', '2102', '2103', '2104', '2105', '2106', '2108', '2109', '2110', '2111', '2112', '2113', '2114', '2115', '2116', '2117', '2118']
def check() :
    for i in range (len(id_list)) :
        if e1.get() == id_list[i-1] : 
            if e2.get() == password_list[i-1] :
                checkLabel["fg"] = "green"
                checkLabel["text"] = "로그인 성공! %s님 안녕하세요" % (id_list[i-1])
                break;
            else : 
                checkLabel["fg"] = "red"
                checkLabel["text"] = "패스워드가 일치하지 않습니다."
                break;
        else : 
            checkLabel["fg"] = "red"
            checkLabel["text"] = "아이디가 일치하지 않습니다."

    

window = Tk()
window.title("LOGIN")
Label(window, text = "아이디").grid(row=0)
Label(window, text = "패스워드").grid(row=1)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

Button(window, text = "Login", command = check).grid(row = 3, column = 0, sticky = W, pady = 4)
Button(window, text = "quit", command = window.quit).grid(row = 3, column = 1, sticky = W, pady = 4)
checkLabel = Label(window, text = "", fg = "green")
checkLabel.grid(row = 3,  column=2)

window.mainloop()