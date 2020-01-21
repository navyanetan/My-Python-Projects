from tkinter import *
root = Tk()
root.title('Calculator')
e= Entry(root, width= 50)
e.grid(row=0,column=0, columnspan=5)


def button_click(number):
    current= e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number)) 
    
def button_clear():
    e.delete(0,END)

def button_A():
    first_number = e.get()
    global f_num
    global math
    math="addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_B():
    first_number = e.get()
    global f_num
    global math
    math="subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_C():
    first_number = e.get()
    global f_num
    global math
    math="multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_D():
    first_number = e.get()
    global f_num
    global math
    math="division"
    f_num = int(first_number)
    e.delete(0, END)

def button_E():
    second_number= e.get()
    e.delete(0, END)
    if math=="addition":
        e.insert(0, f_num + int(second_number))
    elif math=="subtraction":
        e.insert(0, f_num - int(second_number))
    elif math=="multiplication":
        e.insert(0, f_num * int(second_number))
    else:
        e.insert(0, f_num / int(second_number))


button_0 = Button(text='0',padx=50,pady=5,command=lambda: button_click(0))
button_1 = Button(text='1',padx=20,pady=5,command=lambda: button_click(1))
button_2 = Button(text='2',padx=20,pady=5,command=lambda: button_click(2))
button_3 = Button(text='3',padx=20,pady=5,command=lambda: button_click(3))
button_4 = Button(text='4',padx=20,pady=5,command=lambda: button_click(4))
button_5 = Button(text='5',padx=20,pady=5,command=lambda: button_click(5))
button_6 = Button(text='6',padx=20,pady=5,command=lambda: button_click(6))
button_7 = Button(text='7',padx=20,pady=5,command=lambda: button_click(7))
button_8 = Button(text='8',padx=20,pady=5,command=lambda: button_click(8))
button_9 = Button(text='9',padx=20,pady=5,command=lambda: button_click(9))
button_A = Button(text='+',padx=20,pady=5,command=button_A)
button_B = Button(text='-',padx=20,pady=5,command=button_B)
button_C = Button(text='X',padx=20,pady=5,command=button_C)
button_D = Button(text='/',padx=20,pady=5,command=button_D)
button_E = Button(text='=',padx=90,pady=5,command=button_E)
button_F = Button(text='Clear',padx=40,pady=5,command=button_clear)




button_0.grid(row=4, column=0, columnspan=2)
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_A.grid(row=1, column=3)
button_B.grid(row=1, column=4)
button_C.grid(row=2, column=3)
button_D.grid(row=2, column=4)
button_E.grid(row=4, column=2, columnspan=3)
button_F.grid(row=3, column=3, columnspan=2)


root.mainloop()