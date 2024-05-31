import tkinter

import customtkinter as ctk
from tkinter import *
from tkinter import messagebox as mb
import time
from tkinter import font

x = "a"
ctk.set_appearance_mode("Dark")
arr = ['', '', '',
       '', '', '',
       '', '', '',
       ]

class TicTacToe(ctk.CTk):
    global x
    global arr
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("App")
        self.geometry("500x400")
        self.font1 = ctk.CTkFont(slant="italic", family="Helvetica", size=24, weight="bold")
        self.font2 = ctk.CTkFont(size=50, weight="bold")
        self.font3 = ctk.CTkFont(size=50, weight="bold", overstrike=True)

        self.change_int = 0

        self.lab1 = ctk.CTkLabel(self, text="", font=self.font2, width=30, height=20)
        self.lab2 = ctk.CTkLabel(self, text="", font=self.font2, width=30, height=20)
        self.lab3 = ctk.CTkLabel(self, text="", font=self.font2, width=30, height=20)
        self.lab4 = ctk.CTkLabel(self, text="", font=self.font2, width=30, height=20)
        self.lab5 = ctk.CTkLabel(self, text="", font=self.font2, width=30, height=20)
        self.lab6 = ctk.CTkLabel(self, text="", font=self.font2, width=30, height=20)
        self.lab7 = ctk.CTkLabel(self, text="", font=self.font2, width=30, height=20)
        self.lab8 = ctk.CTkLabel(self, text="", font=self.font2, width=30, height=20)
        self.lab9 = ctk.CTkLabel(self, text="", font=self.font2, width=30, height=20)

        self.lab10 = ctk.CTkLabel(self, text="Now placing: o", font=self.font1)
        self.lab11 = ctk.CTkLabel(self, text="")
        self.btn1 = ctk.CTkButton(self, text="⟲", width=1, height=1, fg_color="gray19", command=self.change1)
        self.btn2 = ctk.CTkButton(self, text="⟲", width=1, height=1, fg_color="gray19", command=self.reset)
        self.cv1 = ctk.CTkCanvas(self, width=1, height=178)
        self.cv2 = ctk.CTkCanvas(self, width=1, height=178)
        self.cv3 = ctk.CTkCanvas(self, width=202, height=1)
        self.cv4 = ctk.CTkCanvas(self, width=202, height=1)
        self.cvw1 = ctk.CTkCanvas(self, width=190, height=1, background="gray")
        self.cvw2 = ctk.CTkCanvas(self, width=1, height=170, background="gray")

        self.cv1.place(x=216, y=20)
        self.cv2.place(x=286, y=20)
        self.cv3.place(x=150, y=79)
        self.cv4.place(x=150, y=140)
        self.lab10.place(x=240, y=250, anchor="center")
        self.lab11.grid(column=0, row=0, padx=84)
        self.lab1.grid(column=1, row=0, pady=9)
        self.lab2.grid(column=2, row=0, pady=9)
        self.lab3.grid(column=3, row=0, pady=9)
        self.lab4.grid(column=1, row=1)
        self.lab5.grid(column=2, row=1, padx=40)
        self.lab6.grid(column=3, row=1)
        self.lab7.grid(column=1, row=2, pady=5)
        self.lab8.grid(column=2, row=2, padx=40, pady=5)
        self.lab9.grid(column=3, row=2, pady=5)
        self.btn1.place(x=340, y=250, anchor="center")

        self.lab1.bind("<ButtonPress-1>", self.click1)
        self.lab2.bind("<ButtonPress-1>", self.click2)
        self.lab3.bind("<ButtonPress-1>", self.click3)
        self.lab4.bind("<ButtonPress-1>", self.click4)
        self.lab5.bind("<ButtonPress-1>", self.click5)
        self.lab6.bind("<ButtonPress-1>", self.click6)
        self.lab7.bind("<ButtonPress-1>", self.click7)
        self.lab8.bind("<ButtonPress-1>", self.click8)
        self.lab9.bind("<ButtonPress-1>", self.click9)

    def click1(self, event):
        if self.lab1.cget("text") != "o" and self.lab1.cget("text") != "x":
            if self.change_int == 0:
                self.lab1.configure(text="o")
                self.change()
            elif self.change_int == 1:
                self.lab1.configure(text="x")
                self.change()

    def click2(self, event):
        if self.lab2.cget("text") != "o" and self.lab2.cget("text") != "x":
            if self.change_int == 0:
                self.lab2.configure(text="o")
                self.change()
            elif self.change_int == 1:
                self.lab2.configure(text="x")
                self.change()

    def click3(self, event):
        if self.lab3.cget("text") != "o" and self.lab3.cget("text") != "x":
            if self.change_int == 0:
                self.lab3.configure(text="o")
                self.change()
            elif self.change_int == 1:
                self.lab3.configure(text="x")
                self.change()

    def click4(self, event):
        if self.lab4.cget("text") != "o" and self.lab4.cget("text") != "x":
            if self.change_int == 0:
                self.lab4.configure(text="o")
                self.change()
            elif self.change_int == 1:
                self.lab4.configure(text="x")
                self.change()

    def click5(self, event):
        if self.lab5.cget("text") != "o" and self.lab5.cget("text") != "x":
            if self.change_int == 0:
                self.lab5.configure(text="o")
                self.change()
            elif self.change_int == 1:
                self.lab5.configure(text="x")
                self.change()

    def click6(self, event):
        if self.lab6.cget("text") != "o" and self.lab6.cget("text") != "x":
            if self.change_int == 0:
                self.lab6.configure(text="o")
                self.change()
            elif self.change_int == 1:
                self.lab6.configure(text="x")
                self.change()

    def click7(self, event):
        if self.lab7.cget("text") != "o" and self.lab7.cget("text") != "x":
            if self.change_int == 0:
                self.lab7.configure(text="o")
                self.change()
            elif self.change_int == 1:
                self.lab7.configure(text="x")
                self.change()

    def click8(self, event):
        if self.lab8.cget("text") != "o" and self.lab8.cget("text") != "x":
            if self.change_int == 0:
                self.lab8.configure(text="o")
                self.change()
            elif self.change_int == 1:
                self.lab8.configure(text="x")
                self.change()

    def click9(self, event):
        if self.lab9.cget("text") != "o" and self.lab9.cget("text") != "x":
            if self.change_int == 0:
                self.lab9.configure(text="o")
                self.change()
            elif self.change_int == 1:
                self.lab9.configure(text="x")
                self.change()

    def change(self):
        self.change_int += 1
        if self.change_int > 1:
            self.change_int = 0
        if self.change_int == 0:
            self.lab10.configure(text="Now placing: o")
            x1 = "x"
        if self.change_int == 1:
            self.lab10.configure(text="Now placing: x")
            x1 = "o"
        if self.lab1.cget("text") == x1 and self.lab2.cget("text") == x1 and self.lab3.cget("text") == x1:
            self.lab10.configure(text=f"{x1} won! Reset:")
            self.cvw1.place(x=155, y=41)
            self.btn2.place(x=340, y=250, anchor="center")
            self.btn1.place(x=1000, y=1000, anchor="center")
        elif self.lab4.cget("text") == x1 and self.lab5.cget("text") == x1 and self.lab6.cget("text") == x1:
            self.lab10.configure(text=f"{x1} won! Reset:")
            self.cvw1.place(x=155, y=111)
            self.btn2.place(x=340, y=250, anchor="center")
            self.btn1.place(x=1000, y=1000, anchor="center")
        elif self.lab7.cget("text") == x1 and self.lab8.cget("text") == x1 and self.lab9.cget("text") == x1:
            self.lab10.configure(text=f"{x1} won! Reset:")
            self.cvw1.place(x=155, y=177)
            self.btn2.place(x=340, y=250, anchor="center")
            self.btn1.place(x=1000, y=1000, anchor="center")
        elif self.lab1.cget("text") == x1 and self.lab4.cget("text") == x1 and self.lab7.cget("text") == x1:
            self.lab10.configure(text=f"{x1} won! Reset:")
            self.cvw2.place(x=181, y=24)
            self.btn2.place(x=340, y=250, anchor="center")
            self.btn1.place(x=1000, y=1000, anchor="center")
        elif self.lab2.cget("text") == x1 and self.lab5.cget("text") == x1 and self.lab8.cget("text") == x1:
            self.lab10.configure(text=f"{x1} won! Reset:")
            self.cvw2.place(x=251, y=24)
            self.btn2.place(x=340, y=250, anchor="center")
            self.btn1.place(x=1000, y=1000, anchor="center")
        elif self.lab3.cget("text") == x1 and self.lab6.cget("text") == x1 and self.lab9.cget("text") == x1:
            self.lab10.configure(text=f"{x1} won! Reset:")
            self.cvw2.place(x=321, y=24)
            self.btn2.place(x=340, y=250, anchor="center")
            self.btn1.place(x=1000, y=1000, anchor="center")
        elif self.lab1.cget("text") == x1 and self.lab5.cget("text") == x1 and self.lab9.cget("text") == x1:
            self.lab10.configure(text=f"{x1} won! Reset:")
            self.lab1.configure(font=self.font3)
            self.lab5.configure(font=self.font3)
            self.lab9.configure(font=self.font3)
            self.btn2.place(x=340, y=250, anchor="center")
            self.btn1.place(x=1000, y=1000, anchor="center")
        elif self.lab3.cget("text") == x1 and self.lab5.cget("text") == x1 and self.lab7.cget("text") == x1:
            self.lab10.configure(text=f"{x1} won! Reset:")
            self.lab3.configure(font=self.font3)
            self.lab5.configure(font=self.font3)
            self.lab7.configure(font=self.font3)
            self.btn2.place(x=340, y=250, anchor="center")
            self.btn1.place(x=1000, y=1000, anchor="center")

    def change1(self):
        self.change_int += 1
        if self.change_int > 1:
            self.change_int = 0
        if self.change_int == 0:
            self.lab10.configure(text="Now placing: o")
        if self.change_int == 1:
            self.lab10.configure(text="Now placing: x")

    def reset(self):
        self.btn1.place(x=340, y=250, anchor="center")
        self.btn2.place(x=1000, y=1000, anchor="center")
        self.lab10.configure(text="Now placing: o")
        self.change_int = 0
        self.lab3.configure(font=self.font2, text="")
        self.lab5.configure(font=self.font2, text="")
        self.lab7.configure(font=self.font2, text="")
        self.lab1.configure(font=self.font2, text="")
        self.lab5.configure(font=self.font2, text="")
        self.lab9.configure(font=self.font2, text="")
        self.lab2.configure(text="")
        self.lab4.configure(text="")
        self.lab8.configure(text="")
        self.lab6.configure(text="")
        self.cvw1.place(x=1000, y=1000)
        self.cvw2.place(x=1000, y=1000)

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()


