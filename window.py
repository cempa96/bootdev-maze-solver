from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Window")
        self.canvas = Canvas(width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)    
    
    def redraw(self):
        self.root.update()
        self.root.update_idletasks()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
        self.root.destroy()
    
    def draw_line(self, line:Line, fill_color:str):
        line.draw(self.canvas, fill_color)
            