from tkinter import Canvas
import math

w = 1000
h = 1000

c = Canvas(width = w, height = h)
c.pack()

class C:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __mul__(self, other):
        return C(self.r * other.r - self.i*other.i, self.r*self.i + self.i * other.r)
    def __add__(self, other):
        return C(self.r + other.r, self.i + other.i)
    def __str__(self):
        return f"{self.r} + i{self.i}"
    def abs(self):
        return math.sqrt(self.r**2 + self.i**2)

def mandelbrot_set(depth):
    for i in range(w):
        for j in range(h//2):
            ot = C((i-w/2)/(w/4), (j-(h/2))/(h/4))
            zn = ot
            f = 2
            for n in range(2, depth+1):
                znj = (zn*zn) + ot
                if znj.abs() > 2:
                    break
                f += 1
                zn = znj
            if f == depth+1:
                c.create_rectangle(i, j, i+1, j+1, outline = "black")
                c.create_rectangle(i, h - j, i+1, h + 1-j, outline = "black")
            else:
                farb = 2**24  - 13*2**9*f
                c.create_rectangle(i, j, i+1, j+1, outline = f'#{farb:06x}')
                c.create_rectangle(i, h - j, i+1, h + 1-j, outline = f'#{farb:06x}')


mandelbrot_set(80)
c.mainloop()