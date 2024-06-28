from tkinter import *
import customtkinter as ctk
import random


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("App")
        self.geometry("400x400")

        self.snake = [[9, 9]]
        self.apple = []
        for i in range(0,2):
            self.apple.append(random.randint(0,19))
        self.dir = [1,0]
        self.a=0
        self.cv = ctk.CTkCanvas(self,width=400,height=400,bg="DarkOliveGreen3")

        self.cv.pack()
        self.bind("<KeyPress>",self.check_dir)
        self.main()

    def check_dir(self,event):
        if event.keysym == 'd' and self.dir != [-1,0]:
            self.dir = [1,0]
        elif event.keysym == 'w' and self.dir != [0,1]:
            self.dir = [0,-1]
        elif event.keysym == 'a' and self.dir != [1,0]:
            self.dir = [-1,0]
        elif event.keysym == 's' and self.dir != [0,-1]:
            self.dir = [0,1]

    def new_apple(self):
        self.apple = [random.randint(0,19) for i in range(2)]
        if self.apple in self.snake:
            self.new_apple()

    def create(self):
        self.cv.delete(ALL)
        x=self.apple[0]
        y=self.apple[1]
        self.cv.create_rectangle(x*20, y*20, (x+1)*20,(y+1)*20,fill="firebrick3",width=0)
        for x1, y1 in self.snake:
            self.cv.create_rectangle(x1 * 20, y1 * 20, (x1 + 1) * 20, (y1 + 1) * 20, fill="DodgerBlue2", width=0)

    def check_coord(self,num):
        if num>20 or num<-1:
            self.snake = []
            self.snake.insert(0,[9, 9])
            self.a = 1

    def main(self):
        x, y = self.snake[0]
        x += self.dir[0]
        y += self.dir[1]
        self.check_coord(x)
        self.check_coord(y)
        if self.a == 0:
            self.create()
            if x == self.apple[0] and y == self.apple[1]:
                self.new_apple()
            elif [x,y] in self.snake:
                self.snake = []
                x=9
                y=9
            else:
                self.snake.pop()
            self.snake.insert(0,[x, y])
        elif self.a == 1:
            self.a = 0
        self.cv.after(120,self.main)


if __name__ == "__main__":
    app = App()
    app.mainloop()
