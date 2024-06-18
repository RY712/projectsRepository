import customtkinter as ctk
from tkinter import *
from tkinter import filedialog
import pygame

ctk.set_appearance_mode("Dark")


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pygame.mixer.init()
        self.title("App")
        self.geometry("500x400")

        self.font1 = ctk.CTkFont(slant="italic", family="Helvetica", size=14, weight="bold")
        self.font2 = ctk.CTkFont(slant="roman", family="Times", size=50, weight="bold")
        self.x = ""
        self.audio = ""
        self.y = []
        self.cbb1_var=StringVar()

        self.btn1 = ctk.CTkButton(self, text="START", fg_color="green", corner_radius=25, font=self.font1, width=100,
                                  command=self.start)
        self.btn2 = ctk.CTkButton(self, text="PAUSE", fg_color="green", corner_radius=25, font=self.font1, width=100,
                                  command=self.pause)
        self.btn3 = ctk.CTkButton(self, text="UNPAUSE", fg_color="green", corner_radius=25, font=self.font1, width=100,
                                  command=self.unpause)
        self.btn4 = ctk.CTkButton(self, text="STOP", fg_color="green", corner_radius=25, font=self.font1, width=100,
                                  command=self.stop)
        self.btn5 = ctk.CTkButton(self, text="ADD AN AUDIO FILE", fg_color="green", corner_radius=25, font=self.font1,
                                  width=100, command=self.add_file)

        self.cbb1 = ctk.CTkComboBox(self, fg_color="green", width=200, font=self.font1, values=self.y,
                                    variable=self.cbb1_var)
        self.lb1 = ctk.CTkLabel(self, text="Audio Player🎵", font=self.font2)

        self.lb1.place(x=250, y=30, anchor="center")
        self.cbb1.place(x=250, y=150, anchor="center")
        self.btn1.place(x=60, y=260, anchor="center")
        self.btn2.place(x=185, y=260, anchor="center")
        self.btn3.place(x=310, y=260, anchor="center")
        self.btn4.place(x=435, y=260, anchor="center")
        self.btn5.place(x=250, y=320, anchor="center")

    def start(self):
        self.audio = f"D:/audio/{self.audio}.mp3"
        pygame.mixer.music.load(self.audio)
        pygame.mixer.music.play(loops=0)
        self.audio = self.cbb1_var.get()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def add_file(self):
        self.audio = filedialog.askopenfilename(initialdir='D:/audio/', title="Choose an audio file to add",
                                                filetypes=(("mp3 Files", "*.mp3"),))
        self.audio = self.audio.replace("D:/audio/", "")
        self.audio = self.audio.replace(".mp3", "")
        self.y.append(self.audio)
        self.cbb1.configure(values=self.y)


if __name__ == "__main__":
    app = App()
    app.mainloop()
