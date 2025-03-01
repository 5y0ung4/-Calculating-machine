## 기말고사 팀프로젝트
# 팀3
# 2022111388 임제영, 2022111262 양태원, 2022111746 오서연, 2022111373 박지현
# 기능: 로그, 제곱, 루트, 다크모드, 히스토리


from tkinter import*
from math import*
from time import* 
from tkinter import messagebox

listh = []

## 함수 ##

def click(key) :
    i = 0
    if key == '=':
        result = display.get()
        ##루트계산
        if result[0] == "√":
            result = result[1:]
            result = eval(result)
            s = str(int(result)**(1/2))
            listh.append(s)

        ##제곱 계산 (x제곱 형태)   
        elif '^' in result :
            for i in range(0, len(str(result))):
                if result[i] == '^' :
                    x = int(result[0:i])
                    y = int(result[(i+1):])
                    s = str(x**y)
                    listh.append(s)
                    
        ##로그 계산
        elif result[0:3] == "log":
            result = result[3:]
            result = eval(result)
            s = str(log10(int(result)))
            listh.append(s)
            
        ##사칙연산
        else:
            result = eval(display.get())
            s = str(result)
            listh.append(s)

        ##계산 결과 표현    
        display.delete(0, END)
        display.insert(END, s)

    ##모두 지우기
    elif key == 'C' :
        display.delete(0, END)
        
    else :
        display.insert(END, key)

# 특수계산문자(log, 제곱, 루트)
def root(t = "root") :
    display.insert(END, "√")

def square(t = "sqaure"):
    display.insert(END, '^')


def log(t = 'log') :
    display.insert(END, "log")

# 이전에 계산했던 결과 모두 보기
def history():
    messagebox.showinfo("이전 계산 결과", str(listh))
    
    
    


buttonText = ['7', '8', '9', '/', 'C',
              '4', '5', '6', '*', '  ',
              '1', '2', '3', '-', ' ',
              '0', '.', '=', '+', ' ']


rowindex = 1
colindex =0

## 캔버스 만들기 ##
window = Tk()
window.title("Calculator")
display = Entry(window, width = 33)
display.grid(row=0, column = 0, columnspan =5)


hour = time()
tm = localtime(hour)
if tm.tm_hour >= 19 or tm.tm_hour <= 7:
    display = Entry(window, width = 33, bg = 'black', fg = 'white')
    display.grid(row = 0, column = 0, columnspan = 5)
    
    for button_Text in buttonText :
        def process(t=button_Text) :
            click(t)
        Button(window, text = button_Text, width = 5, command = process, bg = 'black', fg = 'white').grid(row= rowindex, column = colindex)
        colindex += 1
        if colindex > 4 :
            rowindex += 1
            colindex = 0

    button1 = Button(window, text = "root", width = 5, command = root, bg = 'black', fg = 'white').grid(row = 5, column = 0)
    button2 = Button(window, text = "square", width = 5, command = square, bg = 'black', fg = 'white').grid(row = 5, column = 1)
    button3 = Button(window, text = "log", width = 5, command = log, bg = 'black', fg = 'white').grid(row = 5, column = 2)
    button4 = Button(window, text = " ", width = 5, bg = 'black', fg = 'white').grid(row = 5, column = 3)
    button5 = Button(window, text = "", width = 5, bg = 'black', fg = 'white').grid(row = 5, column = 4)


else:
    display = Entry(window, width = 33)
    display.grid(row = 0, column = 0, columnspan = 5)
    for button_Text in buttonText :
        def process(t=button_Text) :
            click(t)
        Button(window, text = button_Text, width = 5, command = process).grid(row= rowindex, column = colindex)
        colindex += 1
        if colindex > 4 :
            rowindex += 1
            colindex = 0
    button1 = Button(window, text = "root", width = 5, command = root).grid(row = 5, column = 0)
    button2 = Button(window, text = "square", width = 5, command = square).grid(row = 5, column = 1)
    button3 = Button(window, text = "log", width = 5, command = log).grid(row = 5, column = 2)
    button4 = Button(window, text = " ", width = 5).grid(row = 5, column = 3)
    button5 = Button(window, text = "", width = 5).grid(row = 5, column = 4)


mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "더보기", menu = fileMenu)
fileMenu.add_command(label = "히스토리 보기", command = history)




window.mainloop()

   
