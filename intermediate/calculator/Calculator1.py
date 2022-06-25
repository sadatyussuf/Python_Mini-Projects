from tkinter import *
from tkinter import ttk
from math import *

expression = ""


def btn_click(num):
    global expression

    expression += str(num)
    equation.set(expression)


def equalto():
    global expression
    try:
        ans = str(eval(expression))
        expression = ans
        equation.set(expression)
    except:
        equation.set("Syntax Error")
        expression = ""


# Deletes the enitre entry
def clear_all():
    global expression
    scrn.delete(0, END)
    expression = ""


def clear():
    global equation
    global expression

    # Removes the last digit from the equation
    expression = equation.get()[:-1]
    # scrn.delete(0,END)
    equation.set(expression)


win = Tk()
win.title("Calculator by Sadat")
# win.resizable(False,False)
# NoteBook
nb = ttk.Notebook(win)

f1 = ttk.Frame(nb)
f1.grid()
f2 = ttk.Frame(nb)
f2.grid()
nb.add(f1)
nb.add(f2)
nb.grid()


def switch():
    nb.select(1)


def switch1():
    nb.select(0)


# Entry to show the values
equation = StringVar()
scrn = Entry(f1, width=45, textvariable=equation, bd=30, insertwidth=4, justify=RIGHT, bg='powder blue',
             font=('arial', 10, 'bold'))  # ,borderwidth=5
scrn.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

# The buttons for the Standard Calculator
btn_1 = Button(f1, text="1", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click(1), font=('arial', 10, 'bold'),
               bg='powder blue')
btn_2 = Button(f1, text="2", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click(2), font=('arial', 10, 'bold'),
               bg='powder blue')
btn_3 = Button(f1, text="3", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click(3), font=('arial', 10, 'bold'),
               bg='powder blue')
btn_4 = Button(f1, text="4", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click(4), font=('arial', 10, 'bold'),
               bg='powder blue')
btn_5 = Button(f1, text="5", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click(5), font=('arial', 10, 'bold'),
               bg='powder blue')
btn_6 = Button(f1, text="6", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click(6), font=('arial', 10, 'bold'),
               bg='powder blue')
btn_7 = Button(f1, text="7", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click(7), font=('arial', 10, 'bold'),
               bg='powder blue')
btn_8 = Button(f1, text="8", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click(8), font=('arial', 10, 'bold'),
               bg='powder blue')
btn_9 = Button(f1, text="9", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click(9), font=('arial', 10, 'bold'),
               bg='powder blue')
btn_0 = Button(f1, text="0", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click(0), font=('arial', 10, 'bold'),
               bg='powder blue')

btn_del = Button(f1, text="DEL", padx=25, pady=10, relief=GROOVE, command=clear_all, font=('arial', 10, 'bold'),
                 bg='red')
btn_div = Button(f1, text="/", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click("/"),
                 font=('arial', 10, 'bold'), bg='orange')
btn_mul = Button(f1, text="x", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click("*"),
                 font=('arial', 10, 'bold'), bg='orange')
btn_add = Button(f1, text="+", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click("+"),
                 font=('arial', 10, 'bold'), bg='orange')
btn_sub = Button(f1, text="-", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click("-"),
                 font=('arial', 10, 'bold'), bg='orange')
btn_dot = Button(f1, text=".", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click("."),
                 font=('arial', 10, 'bold'), bg='orange')
btn_equ = Button(f1, text="=", padx=25, pady=20, relief=GROOVE, command=equalto, font=('arial', 10, 'bold'),
                 bg='orange')

btn_cl = Button(f1, text="C", padx=25, pady=20, relief=GROOVE, command=clear, font=('arial', 10, 'bold'), bg='red')
btn_obra = Button(f1, text="(", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('('),
                  font=('arial', 10, 'bold'), bg='yellow')
btn_cbra = Button(f1, text=")", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click(')'),
                  font=('arial', 10, 'bold'), bg='yellow')
btn_up = Button(f1, text="↑", padx=25, pady=10, relief=GROOVE, font=('arial', 10, 'bold'), bg='green', command=switch)
btn_mod = Button(f1, text="%", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click('%'),
                 font=('arial', 10, 'bold'), bg='yellow')
btn_quo = Button(f1, text="//", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click('//'),
                 font=('arial', 10, 'bold'), bg='yellow')
# btn_00 = Button(win,text="00",padx=25,pady=20,font=('arial',10,'bold'))

# Putting the button widget on the parent widget
btn_del.grid(row=1, column=0, sticky=('N,W,E,S'))
btn_obra.grid(row=1, column=1, sticky=('N,W,E,S'))
btn_cbra.grid(row=1, column=2, sticky=('N,W,E,S'))
btn_up.grid(row=1, column=3, sticky=('N,W,E,S'))

btn_cl.grid(row=2, column=0, sticky=('N,W,E,S'))
btn_mod.grid(row=2, column=1, sticky=('W,E'))
btn_quo.grid(row=2, column=2, sticky=('W,E'))
btn_div.grid(row=2, column=3, sticky=('N,W,E,S'))

btn_7.grid(row=3, column=0, sticky=('N,W,E,S'))
btn_8.grid(row=3, column=1, sticky=('N,W,E,S'))
btn_9.grid(row=3, column=2, sticky=('N,W,E,S'))
btn_mul.grid(row=3, column=3, sticky=('N,W,E,S'))

btn_4.grid(row=4, column=0, sticky=('N,W,E,S'))
btn_5.grid(row=4, column=1, sticky=('N,W,E,S'))
btn_6.grid(row=4, column=2, sticky=('N,W,E,S'))
btn_sub.grid(row=4, column=3, sticky=('N,W,E,S'))

btn_1.grid(row=5, column=0, sticky=('N,W,E,S'))
btn_2.grid(row=5, column=1, sticky=('N,W,E,S'))
btn_3.grid(row=5, column=2, sticky=('N,W,E,S'))
btn_add.grid(row=5, column=3, sticky=('N,W,E,S'))

btn_0.grid(row=6, column=0, sticky=('N,W,E,S'))
btn_dot.grid(row=6, column=1, sticky=('N,W,E,S'))
btn_equ.grid(row=6, column=2, columnspan=2, sticky=('N,W,E,S'))



# The buttons for the Scientific Calculator
scrn = Entry(f2, width=45, textvariable=equation, bd=30, insertwidth=4, justify=RIGHT, bg='powder blue',
             font=('arial', 10, 'bold'), highlightcolor='grey')  # ,borderwidth=5
scrn.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

btn_cl = Button(f2, text="C", padx=25, pady=20, relief=GROOVE, command=clear, font=('arial', 10, 'bold'), bg='red')
btn_obra = Button(f2, text="(", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('('),
                  font=('arial', 10, 'bold'), bg='yellow')
btn_cbra = Button(f2, text=")", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click(')'),
                  font=('arial', 10, 'bold'), bg='yellow')
btn_up = Button(f2, text="↑", padx=25, pady=10, relief=GROOVE, font=('arial', 10, 'bold'), bg='green', command=switch1)
btn_deg = Button(f2, text="deg", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click('degrees('),
                 font=('arial', 10, 'bold'), bg='yellow')
btn_rad = Button(f2, text="rad", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click('radians('),
                 font=('arial', 10, 'bold'), bg='yellow')

btn_del = Button(f2, text="DEL", padx=25, pady=10, relief=GROOVE, command=clear_all, font=('arial', 10, 'bold'),
                 bg='red')
btn_div = Button(f2, text="/", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click("/"),
                 font=('arial', 10, 'bold'), bg='orange')
btn_mul = Button(f2, text="x", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click("*"),
                 font=('arial', 10, 'bold'), bg='orange')
btn_add = Button(f2, text="+", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click("+"),
                 font=('arial', 10, 'bold'), bg='orange')
btn_sub = Button(f2, text="-", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click("-"),
                 font=('arial', 10, 'bold'), bg='orange')
btn_dot = Button(f2, text=".", padx=25, pady=20, relief=GROOVE, command=lambda: btn_click("."),
                 font=('arial', 10, 'bold'), bg='orange')
btn_equ = Button(f2, text="=", padx=25, pady=20, relief=GROOVE, command=equalto, font=('arial', 10, 'bold'),
                 bg='orange')

btn_sq2 = Button(f2, text="X^2", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('**2'),
                 font=('arial', 10, 'bold'), bg='powder blue')
btn_sqn = Button(f2, text="X^n", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('**'),
                 font=('arial', 10, 'bold'), bg='powder blue')
btn_sin = Button(f2, text="sin", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('sin('),
                 font=('arial', 10, 'bold'), bg='powder blue')

btn_exp = Button(f2, text="Exp", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('exp('),
                 font=('arial', 10, 'bold'), bg='powder blue')
btn_pi = Button(f2, text="ח", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('pi'),
                font=('arial', 10, 'bold'), bg='powder blue')
btn_cos = Button(f2, text="cos", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('cos('),
                 font=('arial', 10, 'bold'), bg='powder blue')

btn_tan = Button(f2, text="tan", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('tan('),
                 font=('arial', 10, 'bold'), bg='powder blue')
btn_fac = Button(f2, text="n!", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('factorial('),
                 font=('arial', 10, 'bold'), bg='powder blue')
btn_sqrt = Button(f2, text="√", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('sqrt('),
                  font=('arial', 10, 'bold'), bg='powder blue')

btn_nlog = Button(f2, text="10^ˣ", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('10**'),
                  font=('arial', 10, 'bold'), bg='powder blue')
btn_log = Button(f2, text="log", padx=25, pady=10, relief=GROOVE, command=lambda: btn_click('log10('),
                 font=('arial', 10, 'bold'), bg='powder blue')

btn_del.grid(row=1, column=0, sticky=('N,W,E,S'))
btn_obra.grid(row=1, column=1, sticky=('N,W,E,S'))
btn_cbra.grid(row=1, column=2, sticky=('N,W,E,S'))
btn_up.grid(row=1, column=3, sticky=('N,W,E,S'))

btn_cl.grid(row=2, column=0, sticky=('N,W,E,S'))
btn_deg.grid(row=2, column=1, sticky=('W,E'))
btn_rad.grid(row=2, column=2, sticky=('W,E'))
btn_div.grid(row=2, column=3, sticky=('N,W,E,S'))

btn_sq2.grid(row=3, column=0, sticky=('N,W,E,S'))
btn_sqn.grid(row=3, column=1, sticky=('N,W,E,S'))
btn_sin.grid(row=3, column=2, sticky=('N,W,E,S'))
btn_mul.grid(row=3, column=3, sticky=('N,W,E,S'))

btn_exp.grid(row=4, column=0, sticky=('N,W,E,S'))
btn_pi.grid(row=4, column=1, sticky=('N,W,E,S'))
btn_cos.grid(row=4, column=2, sticky=('N,W,E,S'))
btn_sub.grid(row=4, column=3, sticky=('N,W,E,S'))

btn_tan.grid(row=5, column=0, sticky=('N,W,E,S'))
btn_fac.grid(row=5, column=1, sticky=('N,W,E,S'))
btn_sqrt.grid(row=5, column=2, sticky=('N,W,E,S'))
btn_add.grid(row=5, column=3, sticky=('N,W,E,S'))

btn_nlog.grid(row=6, column=0, sticky=('N,W,E,S'))
btn_log.grid(row=6, column=1, sticky=('N,W,E,S'))
btn_equ.grid(row=6, column=2, columnspan=2, sticky=('N,W,E,S'))
win.mainloop()

"""


btn_pi.grid(row=4,column=0)
"""
