from tkinter import *
from tkinter import ttk,Text
import string,random

Letter = string.ascii_lowercase
Numbers = string.digits
Symbols = string.punctuation

Chara = Letter + Numbers + Symbols

letters =''
numbers = ''
symbols = ''


for char in Chara:
    if char.isalpha():
        letters += char
        #print(letters,end='')
    elif char.isnumeric():
        numbers += char
        #print(numbers,end='')
    else:
        symbols += char
        #print(symbols,end='')
    Chara = {'l':letters,'n':numbers,'s':symbols}


def chck():
    global Chara
    global listofChara
    Chara = {'l': letters, 'n': numbers, 's': symbols}
    if Ch1.get() != 1:
        del Chara['l']

    if Ch2.get() != 1:
        del Chara['n']

    if Ch3.get() != 1:
        del Chara['s']

    listofChara = list(Chara.values())
    random.shuffle(listofChara)
    listofChara = ''.join(listofChara)
def clear():
    txt.delete(1.0,END)

def generate():
    for i in range(int(lenght.get())):
        Password = ""
        results = random.choice(listofChara)
        Password += results
        txt.insert(INSERT,Password)
        #print(Password,end='')

root = Tk()
root.title("Random Password Generator")
root.resizable(False,False)

mainframe = ttk.Frame(root,padding = "3 3 12 12")
mainframe.grid(column = 0,row=0,sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

lenght = StringVar()

ttk.Label(mainframe,text="Lenght: ").grid(column=0,row=0,sticky=E)
lenght_entry = ttk.Entry(mainframe,width=7,textvariable=lenght)
lenght_entry.grid(column=3,row=0,sticky=(W,E))

Ch1= IntVar()
Ch2= IntVar()
Ch3= IntVar()


C1 = Checkbutton(mainframe,text="Alphabets",variable = Ch1,onvalue = 1,offvalue=0,height=5,width=10,command=chck)
C1.grid(column = 0,row=2,sticky=E)
C2 = Checkbutton(mainframe,text="Numbers",variable = Ch2,onvalue = 1,offvalue=0,height=5,width=10,command=chck)
C2.grid(column = 3,row=2,sticky=E)
C3 = Checkbutton(mainframe,text="Symbols",variable = Ch3,onvalue = 1,offvalue=0,height=5,width=10,command=chck)
C3.grid(column = 6,row=2,sticky=E)

txt=Text(mainframe,height=1,width=30,relief=FLAT)
txt.grid(column=0,row=3,columnspan=6)
txt.configure(font=("Times New Roman",12))
ttk.Button(mainframe,text="Generate",command=generate).grid(column = 6,row=3,sticky=E)
ttk.Button(mainframe,text="Clear",command=clear).grid(column = 3,row=4,sticky=W)


root.mainloop()



































































