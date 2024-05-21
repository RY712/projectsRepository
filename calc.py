from tkinter import *
import random
from tkinter.ttk import Combobox, Notebook
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
x=0
y=0
a=0

root=Tk()
root.title("Calculator")
root.geometry("350x365")

def btn_addNum(num):
    global y
    y=y+1
    x1=ent1.get()
    ent1.delete(0,END)
    ent1.insert(0,str(x1)+str(num))

def btn_del():
    global y
    y=y-1
    x1=ent1.get()
    ent1.delete(y,END)

def btn_result():
    global a
    global x
    global y
    x1=ent1.get()
    ent1.delete(0,END)
    if a==1:
        ent1.insert(0,str(x + int(x1)))
    if a==2:
        ent1.insert(0,str(x - int(x1)))
    if a==3:
        ent1.insert(0,str(x * int(x1)))
    if a==4:
        ent1.insert(0,str(int(x / int(x1))))

def btn_div():
    global x
    global y
    global a
    y = 0
    x1 = ent1.get()
    a = 4
    x = int(x1)
    ent1.delete(0, END)


def btn_min():
    global x
    global y
    global a
    y = 0
    x1=ent1.get()
    a=2
    x=int(x1)
    ent1.delete(0,END)


def btn_plus():
    global x
    global a
    global y
    y = 0
    x1=ent1.get()
    a=1
    x=int(x1)
    ent1.delete(0,END)


def btn_mult():
    global x
    global a
    global y
    y=0
    x1=ent1.get()
    a=3
    x=int(x1)
    ent1.delete(0,END)



root.config(bg="dimgray")

fr1=Frame(root,width=350,height=325,bg="dimgray")
fr1.grid(pady=75)

ent1=Entry(root,bg="snow4",fg="white",width=15,font=("Arial",30),relief=SUNKEN)

ent1.place(x=175,y=45,anchor="center")

btn1=Button(fr1,text="7",width=8,height=3,font=20,bg="silver",activebackground="snow4",command=lambda: btn_addNum(7))
btn1.grid(row=0,column=0,padx=4,pady=2)
btn2=Button(fr1,text="8",width=8,height=3,font=20,bg="silver",activebackground="snow4",command=lambda: btn_addNum(8))
btn2.grid(row=0,column=1,padx=2,pady=2)
btn3=Button(fr1,text="9",width=8,height=3,font=20,bg="silver",activebackground="snow4",command=lambda: btn_addNum(9))
btn3.grid(row=0,column=2,padx=2,pady=2)
btn4=Button(fr1,text="⌫",width=8,height=3,font=20,bg="snow4",activebackground="silver",command=btn_del)
btn4.grid(row=0,column=4,padx=2,pady=2)

btn5=Button(fr1,text="4",width=8,height=3,font=20,bg="silver",activebackground="snow4",command=lambda: btn_addNum(4))
btn5.grid(row=1,column=0,padx=2,pady=2)
btn6=Button(fr1,text="5",width=8,height=3,font=20,bg="silver",activebackground="snow4",command=lambda: btn_addNum(5))
btn6.grid(row=1,column=1,padx=2,pady=2)
btn7=Button(fr1,text="6",width=8,height=3,font=20,bg="silver",activebackground="snow4",command=lambda: btn_addNum(6))
btn7.grid(row=1,column=2,padx=2,pady=2)
btn8=Button(fr1,text="=",width=8,height=3,font=20,bg="snow4",activebackground="silver",command=btn_result)
btn8.grid(row=1,column=4,padx=2,pady=2)

btn9=Button(fr1,text="1",width=8,height=3,font=20,bg="silver",activebackground="snow4",command=lambda: btn_addNum(1))
btn9.grid(row=2,column=0,padx=2,pady=2)
btn10=Button(fr1,text="2",width=8,height=3,font=20,bg="silver",activebackground="snow4",command=lambda: btn_addNum(2))
btn10.grid(row=2,column=1,padx=2,pady=2)
btn11=Button(fr1,text="3",width=8,height=3,font=20,bg="silver",activebackground="snow4",command=lambda: btn_addNum(3))
btn11.grid(row=2,column=2,padx=2,pady=2)
btn12=Button(fr1,text="÷",width=8,height=3,font=20,bg="snow4",activebackground="silver",command=btn_div)
btn12.grid(row=2,column=4,padx=2,pady=2)

btn13=Button(fr1,text="-",width=8,height=3,font=20,bg="snow4",activebackground="silver",command=btn_min)
btn13.grid(row=3,column=0,padx=2,pady=2)
btn14=Button(fr1,text="0",width=8,height=3,font=20,bg="silver",activebackground="snow4",command=lambda: btn_addNum(0))
btn14.grid(row=3,column=1,padx=2,pady=2)
btn15=Button(fr1,text="+",width=8,height=3,font=20,bg="snow4",activebackground="silver",command=btn_plus)
btn15.grid(row=3,column=2,padx=2,pady=2)
btn16=Button(fr1,text="×",width=8,height=3,font=20,bg="snow4",activebackground="silver",command=btn_mult)
btn16.grid(row=3,column=4,padx=2,pady=2)

root.mainloop()




















