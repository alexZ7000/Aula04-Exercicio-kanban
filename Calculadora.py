from tkinter import *
root = Tk()
root.title("Calculadora Kanban")

root.config(bg="lightblue")
e = Entry(root, font=50, width=25, borderwidth=10, bg="gray", fg="white")
e.grid(row=0, column=0, columnspan=5, padx=20, pady=10)

def bAdd(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def bSub():
    num1 = e.get()
    global f_num
    global math
    global var_controle
    global temp
    math = "subtraction"
    if num1 == '':
        temp = 0
        e.delete(0, END)
    else:
        f_num = int(num1)
        e.delete(0, END)

def bIgual():
    num2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(num2))
    if math == "multiplication":
        e.insert(0, f_num * int(num2))
    if math == "division":
        e.insert(0, f_num / int(num2))
    if math == "subtraction":
        e.insert(0, (f_num) - int(num2))

def bDelete():
    e.delete(first=0)

def bClear():
    e.delete(0, END)

def bSoma():
    num1 = e.get()
    global f_num #Podemos usar global fora da função
    global math
    math = "addition"
    f_num = int(num1)
    e.delete(0, END)

def bIgual():
    num2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(num2))
    if math == "multiplication":
        e.insert(0, f_num * int(num2))
    if math == "division":
        e.insert(0, f_num / int(num2))
    if math == "subtraction":
        e.insert(0, (f_num) - int(num2))

def bMult():
    num1 = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(num1)
    e.delete(0, END)

def bDiv():
    num1 = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(num1)
    e.delete(0, END)

b0 = Button(root, font=10, text="0", borderwidth=6,  width=8, height=4, command=lambda: bAdd(0), bg="lightgray")
b1 = Button(root, font=10, text="1", borderwidth=6,  width=8, height=4, command=lambda: bAdd(1), bg="lightgray")
b2 = Button(root, font=10, text="2", borderwidth=6,  width=8, height=4, command=lambda: bAdd(2), bg="lightgray")
b3 = Button(root, font=10, text="3", borderwidth=6,  width=8, height=4, command=lambda: bAdd(3), bg="lightgray")
b4 = Button(root, font=10, text="4", borderwidth=6,  width=8, height=4, command=lambda: bAdd(4), bg="lightgray")
b5 = Button(root, font=10, text="5", borderwidth=6,  width=8, height=4, command=lambda: bAdd(5), bg="lightgray")
b6 = Button(root, font=10, text="6", borderwidth=6,  width=8, height=4, command=lambda: bAdd(6), bg="lightgray")
b7 = Button(root, font=10, text="7", borderwidth=6,  width=8, height=4, command=lambda: bAdd(7), bg="lightgray")
b8 = Button(root, font=10, text="8", borderwidth=6,  width=8, height=4, command=lambda: bAdd(8), bg="lightgray")
b9 = Button(root, font=10, text="9", borderwidth=6,  width=8, height=4, command=lambda: bAdd(9), bg="lightgray")
b10 = Button(root, font=10, text="=", borderwidth=6,  width=8, height=4, command=bIgual, bg="lightgreen")
b11 = Button(root, font=10, text="+", borderwidth=6,  width=8, height=4, command=bSoma, bg="gray")
b12 = Button(root, font=10, text="-", borderwidth=6,  width=8, height=4, command=bSub, bg="gray")
b13 = Button(root, font=10, text="*", borderwidth=6,  width=8, height=4, command=bMult, bg="gray")
b14 = Button(root, font=10, text="/", borderwidth=6,  width=8, height=4, command=bDiv, bg="gray")
b15 = Button(root, font=10, text="CE", borderwidth=6,  width=8, height=4, command=bClear, bg="gray")
b16 = Button(root, font=10, text="<", borderwidth=6,  width=8, height=4, command=bDelete, bg="#F08080")

b0.grid(row=5, column=1, padx=1.25, pady=1.25)
b1.grid(row=4, column=0, padx=1.25, pady=1.25)
b2.grid(row=4, column=1, padx=1.25, pady=1.25)
b3.grid(row=4, column=2, padx=1.25, pady=1.25)
b4.grid(row=3, column=0, padx=1.25, pady=1.25)
b5.grid(row=3, column=1, padx=1.25, pady=1.25)
b6.grid(row=3, column=2, padx=1.25, pady=1.25)
b7.grid(row=2, column=0, padx=1.25, pady=1.25)
b8.grid(row=2, column=1, padx=1.25, pady=1.25)
b9.grid(row=2, column=2, padx=1.25, pady=1.25)
b10.grid(row=5, column=3, padx=1.25, pady=1.25)
b11.grid(row=4, column=3, padx=1.25, pady=1.25)
b12.grid(row=3, column=3, padx=1.25, pady=1.25)
b13.grid(row=2, column=3, padx=1.25, pady=1.25)
b14.grid(row=5, column=0, padx=1.25, pady=1.25)
b15.grid(row=1, column=0, padx=1.25, pady=1.25)
b16.grid(row=5, column=2, padx=1.25, pady=1.25)

root.mainloop()
