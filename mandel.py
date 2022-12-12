from tkinter import Canvas
import math

c = Canvas(width = 1500, height = 1500)
c.pack()

class C:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __mul__(self, other):
        return C(self.r * other.r - self.i*other.i, self.r*self.i + self.i * other.r)
    def __str__(self):
        return f"{self.r} + i{self.i}"
c.mainloop()