from gtts import gTTS
import os
import customtkinter as ctk
from tkinter import *
from tkinter import filedialog
import pygame

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("App")
        pygame.mixer.init()
        self.geometry("500x400")

        self.font1 = ctk.CTkFont(slant="italic", family="Helvetica", size=14, weight="bold")
        self.font2 = ctk.CTkFont(slant="roman", family="Times", size=50, weight="bold")
        self.f1=""
        self.x=0
        self.y=0
        self.f2=""
        self.txt=""

        self.lab=ctk.CTkLabel(self,text="Text-To-Speech",font=self.font2)
        self.txt1 = ctk.CTkTextbox(self,width=350,height=240,font=self.font1)
        self.btn1 = ctk.CTkButton(self,text="Save file", fg_color="green",font=self.font1,command=self.save)
        self.btn2 = ctk.CTkButton(self,text="Choose file", fg_color="green",font=self.font1,command=self.choose)
        self.btn3 = ctk.CTkButton(self,text="Play", fg_color="green",width=80,font=self.font1,command=self.start)
        self.btn4 = ctk.CTkButton(self,text="Pause", fg_color="green",width=80,font=self.font1,command=self.pause)
        self.btn5 = ctk.CTkButton(self,text="Unpause", fg_color="green",width=80,font=self.font1,command=self.unpause)
        self.btn6 = ctk.CTkButton(self,text="Stop", fg_color="green",width=80,font=self.font1,command=self.stop)
        self.audio = gTTS(text="a",lang="en",slow=False)

        self.lab.place(x=250,y=25,anchor="center")
        self.txt1.place(x=250,y=190,anchor="center")
        self.btn1.place(x=166,y=320,anchor="center")
        self.btn2.place(x=332, y=320, anchor="center")
        self.btn3.place(x=100,y=360,anchor="center")
        self.btn4.place(x=200, y=360, anchor="center")
        self.btn5.place(x=300,y=360,anchor="center")
        self.btn6.place(x=400, y=360, anchor="center")

    def save(self):
        self.f1=open(f"text{self.x}.txt",'w')
        self.f1.write(self.txt1.get("1.0","end"))
        self.f1.close()
        self.x=self.x+1

    def choose(self):
        self.f2 = filedialog.askopenfilename(initialdir='C:/Users/andre/PycharmProjects/main', title="Choose a file to convert",
                                             filetypes=(("txt Files", "*.txt"),))
        self.f2.replace("C:/Users/andre/PycharmProjects/main/","")
        self.f1=open(self.f2,'r')
        self.txt=self.f1.read()
        self.audio = gTTS(text=self.txt,lang="en",slow=False)
        self.y=self.y+1
        self.audio.save(f"audio{self.y}.mp3")
        self.f1.close()
        self.txt1.delete("1.0","end")
        self.txt1.insert("1.0",self.txt)

    def start(self):
        pygame.mixer.music.load(f"audio{self.y}.mp3")
        pygame.mixer.music.play(loops=0)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    app = App()
    app.mainloop()


