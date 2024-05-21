import customtkinter as ctk
from tkinter import *
from tkinter import messagebox as mb
import time
from tkinter import font

ctk.set_appearance_mode("Dark")

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("App")
        self.geometry("500x400")
        self.main_menu = Menu()
        self.main_menu.add_command(label="Timer",command=self.start_timer)
        self.main_menu.add_command(label="Stopwatch",command=self.start_stopwatch)
        self.config(menu=self.main_menu)

        self.fr1 = ctk.CTkFrame(self, width=500, height=400)
        self.fr2 = ctk.CTkFrame(self, width=500, height=400)

        self.stop_int1=0
        self.sec_total1=0
        self.x1=[]
        self.set_time1=0

        self.font1=ctk.CTkFont(slant="italic",family="Helvetica",size=24,weight="bold")
        self.font2 = ctk.CTkFont(slant="roman", family="Times", size=50, weight="bold")

        self.lab5=ctk.CTkLabel(self.fr1,text="Timer",font=self.font2)
        self.lab6 = ctk.CTkLabel(self.fr2, text="Timer", font=self.font2)
        self.ent2 = ctk.CTkEntry(self.fr1,font=self.font1)
        self.ent3 = ctk.CTkEntry(self.fr1,font=self.font1)
        self.ent4 = ctk.CTkEntry(self.fr1,font=self.font1)
        self.lab1 = ctk.CTkLabel(self.fr1, text="Hours",font=self.font1)
        self.lab2 = ctk.CTkLabel(self.fr1, text="Minutes",font=self.font1)
        self.lab3 = ctk.CTkLabel(self.fr1, text="Seconds",font=self.font1)
        self.btn3 = ctk.CTkButton(self.fr1, text="Start", width=100, height=25,fg_color="green",corner_radius=100,
                                  command=self.start1,font=self.font1)
        self.btn3.place(x=250, y=300, anchor="center")
        self.ent2.place(x=100, y=200, anchor="center")
        self.ent3.place(x=250, y=200, anchor="center")
        self.ent4.place(x=400, y=200, anchor="center")
        self.lab1.place(x=100, y=160, anchor="center")
        self.lab2.place(x=250, y=160, anchor="center")
        self.lab3.place(x=400, y=160, anchor="center")
        self.lab5.place(x=250, y=25, anchor="center")

        self.btn1 = ctk.CTkButton(self.fr2, text="Stop", width=100, height=25,fg_color="green",corner_radius=10,
                                  command=self.stop1,font=self.font1)
        self.btn1.place(x=250, y=300, anchor="center")
        self.ent1 = ctk.CTkEntry(self.fr2,font=self.font1)
        self.ent1.place(x=250, y=175, anchor="center")
        self.lab6.place(x=250, y=25, anchor="center")

        self.lab4 = ctk.CTkLabel(self.fr2, text="")
        self.lab4.place(x=250, y=150, anchor="center")

        #=================================================

        self.fr3 = ctk.CTkFrame(self, width=500, height=400)
        self.fr4 = ctk.CTkFrame(self, width=500, height=400)

        self.stop_int2=0
        self.sec_total2=0
        self.x2=[]
        self.set_time2=0

        self.lab7 = ctk.CTkLabel(self.fr3, text="Stopwatch", font=self.font2)
        self.lab8 = ctk.CTkLabel(self.fr4, text="Stopwatch", font=self.font2)
        self.btn2 = ctk.CTkButton(self.fr3, text="Start", width=150, height=35, fg_color="green", corner_radius=100,
                                  command=self.start2, font=self.font1)
        self.btn4 = ctk.CTkButton(self.fr4, text="Stop", width=100, height=25,fg_color="green",corner_radius=10,
                                  command=self.stop2,font=self.font1)
        self.ent5 = ctk.CTkEntry(self.fr4,font=self.font1)

        self.btn2.place(x=250, y=200, anchor="center")
        self.lab7.place(x=250, y=25, anchor="center")
        self.lab8.place(x=250, y=25, anchor="center")
        self.ent5.place(x=250, y=175, anchor="center")
        self.btn4.place(x=250, y=300, anchor="center")

    def start_timer(self):
        self.fr2.place(x=1500,y=1500)
        self.fr1.pack()
        self.fr3.place(x=1500, y=1500)
        self.fr4.place(x=1500, y=1500)

    def start_stopwatch(self):
        self.fr1.place(x=1500,y=1500)
        self.fr2.place(x=1500, y=1500)
        self.fr3.pack()
        self.fr4.place(x=1500, y=1500)

    def stop1(self):
        self.ent2.delete(0, END)
        self.ent3.delete(0, END)
        self.ent4.delete(0, END)
        self.fr2.place(x=1000, y=1000)
        self.fr1.pack()
        self.stop_int1 = 1

    def stop2(self):
        self.fr4.place(x=1000, y=1000)
        self.fr3.pack()
        self.stop_int2 = 1

    def start1(self):
        self.fr1.place(x=1000, y=1000)
        self.fr2.pack()
        self.ent1.delete(0,END)
        try:
            self.sec_total1 = int(self.ent2.get()) * 3600 + int(self.ent3.get()) * 60 + int(self.ent4.get())
        except:
            mb.showwarning('', 'Invalid Input!')
        while self.sec_total1 > -1:
            if self.stop_int1 == 1:
                self.stop_int1 = 0
                break
            self.x1.clear()
            self.ent1.delete(0, END)
            m, s = divmod(self.sec_total1, 60)
            h = 0
            if m > 59:
                h, m = divmod(m, 60)
            if h < 10:
                h1 = f"0{str(h)}"
            else:
                h1 = str(h)
            if m < 10:
                m1 = f"0{str(m)}"
            else:
                m1 = str(m)
            if s < 10:
                s1 = f"0{str(s)}"
            else:
                s1 = str(s)
            self.x1.append(h1)
            self.x1.append(m1)
            self.x1.append(s1)
            self.set_time1 = ':'.join(self.x1)
            self.ent1.insert(0, self.set_time1)

            self.update()
            time.sleep(1)
            if self.sec_total1 == 0:
                mb.showinfo("", "Time's up")
                self.fr2.place(x=1000, y=1000)
                self.fr1.pack()
                self.ent2.delete(0, END)
                self.ent3.delete(0, END)
                self.ent4.delete(0, END)

            self.sec_total1 = self.sec_total1 - 1

    def start2(self):
        m=0
        self.fr3.place(x=1000, y=1000)
        self.fr4.pack()
        self.ent5.delete(0, END)
        self.sec_total2=0
        while True:
            if self.stop_int1 == 1:
                self.stop_int1 = 0
                break
            self.x2.clear()
            self.ent5.delete(0, END)
            if self.sec_total2>59:
                m, s = divmod(self.sec_total2, 60)
            else:
                s = self.sec_total2
            h = 0
            if m > 59:
                h, m = divmod(m, 60)
            if h < 10:
                h1 = f"0{str(h)}"
            else:
                h1 = str(h)
            if m < 10:
                m1 = f"0{str(m)}"
            else:
                m1 = str(m)
            if s < 10:
                s1 = f"0{str(s)}"
            else:
                s1 = str(s)
            self.x2.append(h1)
            self.x2.append(m1)
            self.x2.append(s1)
            self.set_time2 = ':'.join(self.x2)
            self.ent5.insert(0, self.set_time2)

            self.update()
            time.sleep(1)
            self.sec_total2 = self.sec_total2 + 1



if __name__ == "__main__":
    app = App()
    app.mainloop()


