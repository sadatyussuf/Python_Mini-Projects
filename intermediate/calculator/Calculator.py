from tkinter import  *
from math import *
from math import factorial as fac
from math import degrees as deg
from math import radians as rad
expression=""

def btn_click(num):
    global expression

    expression+=str(num)
    equation.set(expression)

def equalto():
    global expression
    global s_ans
    try:
        ans = str(eval(expression))
        expression=ans
        s_ans=expression
        equation.set(expression)
        expression=""
    except:
        equation.set("Syntax Error")
        expression=""


def store_ans():
    global s_ans, expression
    expression+= s_ans
    equation.set(expression)

def sq():
    if text['key']=='sqrt':
        pass

#Deletes the enitre entry
def clear_all():
    global expression
    scrn.delete(0,END)
    expression = ""

def clear():
    global equation
    global expression

#Removes the last digit from the equation
    expression=equation.get()[:-1]
    #scrn.delete(0,END)
    equation.set(expression)

def standard():
    win.resizable(False, False)
    win.geometry("400x475+0+0")


def scientific():
    win.resizable(False, False)
    win.geometry("1010x568+0+0")


win = Tk()
win.title("Calculator by Sadat")
win.resizable(False,False)
win.geometry("400x475+0+0")
win.option_add('*tearOff', FALSE)


#The Frame
cal_frame = Frame(win,bg='black')
cal_frame.grid(sticky=('N,W,E,S'))

#-----------------------------------The Menubar------------------------------------------------------
cal_menu = Menu(cal_frame)
cal_file = Menu(cal_menu)
cal_edit = Menu(cal_menu)
cal_help = Menu(cal_menu)


#File menubar
cal_menu.add_cascade(label='File',menu=cal_file)
cal_file.add_command(label="Standard",command=standard)
cal_file.add_command(label="Scientific",command=scientific)
cal_file.add_separator()
cal_file.add_command(label="Exit",command=win.destroy)

#Edit menubar
cal_menu.add_cascade(label='Edit',menu=cal_edit)
cal_edit.add_command(label="Cut")
cal_edit.add_command(label="Copy")
cal_edit.add_separator()
cal_edit.add_command(label="Paste")

#Help menubar
cal_menu.add_cascade(label='Help',menu=cal_help)
cal_help.add_command(label="View Help")
cal_help.add_command(label="Copy")

#----------------------------------------------Entry to show the values-----------------------------------------------------
equation = StringVar()
scrn = Entry(cal_frame,width = 45,textvariable=equation,bd=30,insertwidth=4,justify=RIGHT,bg='powder blue',font=('arial',10,'bold'))#,borderwidth=5
scrn.grid(column =0,row=0,columnspan=4,padx=10,pady=10,sticky=('N,W,E,S'))
scrn.insert(0,'0')
#--------------------------------The buttons for the Standard Calculator------------------------------------------------------------
label=Label(cal_frame,text="STANDARD CALCULATOR",justify=CENTER,bg='powder blue',font=('arial',20,'bold'))
label.grid(row=7,column=0,columnspan=4,sticky=('N,W,E,S'))

btn_1 = Button(cal_frame,text="1",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click(1),font=('arial',10,'bold'),bg='powder blue')
btn_2 = Button(cal_frame,text="2",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click(2),font=('arial',10,'bold'),bg='powder blue')
btn_3 = Button(cal_frame,text="3",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click(3),font=('arial',10,'bold'),bg='powder blue')
btn_4 = Button(cal_frame,text="4",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click(4),font=('arial',10,'bold'),bg='powder blue')
btn_5 = Button(cal_frame,text="5",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click(5),font=('arial',10,'bold'),bg='powder blue')
btn_6 = Button(cal_frame,text="6",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click(6),font=('arial',10,'bold'),bg='powder blue')
btn_7 = Button(cal_frame,text="7",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click(7),font=('arial',10,'bold'),bg='powder blue')
btn_8 = Button(cal_frame,text="8",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click(8),font=('arial',10,'bold'),bg='powder blue')
btn_9 = Button(cal_frame,text="9",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click(9),font=('arial',10,'bold'),bg='powder blue')
btn_0 = Button(cal_frame,text="0",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click(0),font=('arial',10,'bold'),bg='powder blue')

btn_del = Button(cal_frame,text=chr(67)+chr(69),padx=25,pady=10,relief= GROOVE,command=clear_all,font=('arial',10,'bold'),bg='red')
btn_div = Button(cal_frame,text=chr(247),padx=25,pady=20,relief= GROOVE,command=lambda:btn_click("/"),font=('arial',10,'bold'),bg='orange')
btn_mul = Button(cal_frame,text="x",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click("*"),font=('arial',10,'bold'),bg='orange')
btn_add = Button(cal_frame,text="+",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click("+"),font=('arial',10,'bold'),bg='orange')
btn_sub = Button(cal_frame,text="-",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click("-"),font=('arial',10,'bold'),bg='orange')
btn_dot = Button(cal_frame,text=".",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click("."),font=('arial',10,'bold'),bg='orange')
btn_equ = Button(cal_frame,text="=",padx=25,pady=20,relief= GROOVE,command=equalto,font=('arial',10,'bold'),bg='orange')

btn_cl = Button(cal_frame,text=chr(67),padx=25,pady=20,relief= GROOVE,command=clear,font=('arial',10,'bold'),bg='red')
btn_obra = Button(cal_frame,text="(",padx=25,pady=10,relief= GROOVE,command=lambda:btn_click('('),font=('arial',10,'bold'),bg='yellow')
btn_cbra = Button(cal_frame,text=")",padx=25,pady=10,relief= GROOVE,command=lambda:btn_click(')'),font=('arial',10,'bold'),bg='yellow')
btn_ans = Button(cal_frame,text="ANS",padx=25,pady=10,relief= GROOVE,command=store_ans,font=('arial',10,'bold'),bg='green')
btn_mod = Button(cal_frame,text="%",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click('%'),font=('arial',10,'bold'),bg='yellow')
btn_quo = Button(cal_frame,text=",",padx=25,pady=20,relief= GROOVE,command=lambda:btn_click(','),font=('arial',10,'bold'),bg='yellow')


#Putting the button widget on the parent widget
btn_del.grid(row=1,column=0,sticky=('N,W,E,S'))
btn_obra.grid(row=1,column=1,sticky=('N,W,E,S'))
btn_cbra.grid(row=1,column=2,sticky=('N,W,E,S'))
btn_ans.grid(row=1,column=3,sticky=('N,W,E,S'))

btn_cl.grid(row=2,column=0,sticky=('N,W,E,S'))
btn_mod.grid(row=2,column=1,sticky=('W,E'))
btn_quo.grid(row=2,column=2,sticky=('W,E'))
btn_div.grid(row=2,column=3,sticky=('N,W,E,S'))

btn_7.grid(row=3,column=0,sticky=('N,W,E,S'))
btn_8.grid(row=3,column=1,sticky=('N,W,E,S'))
btn_9.grid(row=3,column=2,sticky=('N,W,E,S'))
btn_mul.grid(row=3,column=3,sticky=('N,W,E,S'))

btn_4.grid(row=4,column=0,sticky=('N,W,E,S'))
btn_5.grid(row=4,column=1,sticky=('N,W,E,S'))
btn_6.grid(row=4,column=2,sticky=('N,W,E,S'))
btn_sub.grid(row=4,column=3,sticky=('N,W,E,S'))

btn_1.grid(row=5,column=0,sticky=('N,W,E,S'))
btn_2.grid(row=5,column=1,sticky=('N,W,E,S'))
btn_3.grid(row=5,column=2,sticky=('N,W,E,S'))
btn_add.grid(row=5,column=3,sticky=('N,W,E,S'))

btn_0.grid(row=6,column=0,sticky=('N,W,E,S'))
btn_dot.grid(row=6,column=1,sticky=('N,W,E,S'))
btn_equ.grid(row=6,column=2,columnspan=2,sticky=('N,W,E,S'))

#----------------------------------------The Buttons for the Scientific Calculator-----------------------------------------------
label=Label(cal_frame,text="SCIENTIFIC CALCULATOR",justify=CENTER,bg='powder blue',font=('arial',20,'bold'))
label.grid(row=0,column=5,columnspan=5)

btn_sq2 = Button(cal_frame, text="X^2", padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('**2'))
btn_sqn = Button(cal_frame,text="X^n",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click("**"))
btn_sin = Button(cal_frame,text="sin(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('sin('))
btn_cos = Button(cal_frame,text="cos(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('cos('))

btn_tan = Button(cal_frame,text="tan",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('tan('))
btn_sqrt = Button(cal_frame,text="√",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('sqrt('))
btn_nlog = Button(cal_frame,text="10^ˣ",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('10**'))
btn_log = Button(cal_frame,text="log",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('log('))

btn_exp = Button(cal_frame,text="Exp(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('exp('))
btn_pi = Button(cal_frame,text="pi",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click(pi))
btn_fac = Button(cal_frame,text="n!",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('fac('))
btn_acosh = Button(cal_frame,text="acosh(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('acosh('))

btn_asinh = Button(cal_frame,text="asinh(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('asinh('))
btn_atanh = Button(cal_frame,text="atanh(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('atanh('))
btn_tanh = Button(cal_frame,text="tanh(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('tanh('))
btn_log10 = Button(cal_frame,text="log10(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('log10('))

btn_log1p = Button(cal_frame,text="log1p(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('log1p('))
btn_sinh = Button(cal_frame,text="sinh(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('sinh('))
btn_cosh = Button(cal_frame,text="cosh(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('cosh('))
btn_asin = Button(cal_frame,text="asin(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('asin('))

btn_acos = Button(cal_frame,text="acos(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('acos('))
btn_atan = Button(cal_frame,text="atan(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('atan('))
btn_atan2 = Button(cal_frame,text="atan2(x,y)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('atan2('))
btn_ceil = Button(cal_frame,text="ceil(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('ceil('))

btn_floor = Button(cal_frame,text="floor(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('floor('))
btn_expm1 = Button(cal_frame,text="expm1(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('expm1('))
btn_abs = Button(cal_frame,text="abs(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('abs('))
btn_gamma = Button(cal_frame,text="gamma(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('gamma('))

btn_hypot = Button(cal_frame,text="hypoth(x,y)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('hypot('))
btn_E = Button(cal_frame,text="E",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click(e))
btn_gcd = Button(cal_frame,text="gcd(x,y)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('gcd('))
btn_pow = Button(cal_frame,text="pow(x,y)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('pow('))

btn_degrees = Button(cal_frame,text="degrees(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('deg('))
btn_radians = Button(cal_frame,text="radians(x)",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click('rad('))
btn_00 = Button(cal_frame,text="00",padx=25,pady=20,font=('arial',10,'bold'),bg='powder blue',command=lambda:btn_click(00))

btn_sq2.grid(row=1,column=4,sticky=('N,W,E,S'))
btn_sqn.grid(row=1,column=5,sticky=('N,W,E,S'))
btn_fac.grid(row=1,column=6,sticky=('N,W,E,S'))
btn_sqrt.grid(row=1,column=7,sticky=('N,W,E,S'))
btn_hypot.grid(row=1,column=8,sticky=('N,W,E,S'))

btn_sin.grid(row=2,column=4,sticky=('N,W,E,S'))
btn_cos.grid(row=2,column=5,sticky=('N,W,E,S'))
btn_tan.grid(row=2,column=6,sticky=('N,W,E,S'))
btn_nlog.grid(row=2,column=7,sticky=('N,W,E,S'))
btn_E.grid(row=2,column=8,sticky=('N,W,E,S'))

btn_log.grid(row=3,column=4,sticky=('N,W,E,S'))
btn_exp.grid(row=3,column=5,sticky=('N,W,E,S'))
btn_pi.grid(row=3,column=6,sticky=('N,W,E,S'))
btn_log10.grid(row=3,column=7,sticky=('N,W,E,S'))
btn_gamma.grid(row=3,column=8,sticky=('N,W,E,S'))

btn_acosh.grid(row=4,column=4,sticky=('N,W,E,S'))
btn_asinh.grid(row=4,column=5,sticky=('N,W,E,S'))
btn_atanh.grid(row=4,column=6,sticky=('N,W,E,S'))
btn_tanh.grid(row=4,column=7,sticky=('N,W,E,S'))
btn_abs.grid(row=4,column=8,sticky=('N,W,E,S'))

btn_sinh.grid(row=5,column=4,sticky=('N,W,E,S'))
btn_cosh.grid(row=5,column=5,sticky=('N,W,E,S'))
btn_acos.grid(row=5,column=6,sticky=('N,W,E,S'))
btn_atan.grid(row=5,column=7,sticky=('N,W,E,S'))
btn_expm1.grid(row=5,column=8,sticky=('N,W,E,S'))

btn_asin.grid(row=6,column=4,sticky=('N,W,E,S'))
btn_atan2.grid(row=6,column=5,sticky=('N,W,E,S'))
btn_log1p.grid(row=6,column=6,sticky=('N,W,E,S'))
btn_ceil.grid(row=6,column=7,sticky=('N,W,E,S'))
btn_floor.grid(row=6,column=8,sticky=('N,W,E,S'))

btn_00.grid(row=7,column=4,sticky=('N,W,E,S'))
btn_gcd.grid(row=7,column=5,sticky=('N,W,E,S'))
btn_pow.grid(row=7,column=6,sticky=('N,W,E,S'))
btn_degrees.grid(row=7,column=7,sticky=('N,E,S'))
btn_radians.grid(row=7,column=8,sticky=('N,W,E,S'))

win.config(menu=cal_menu)
win.mainloop()

"""


"""