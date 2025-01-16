from tkinter import Canvas
import math
import time

w = 1500
h = 1500

canvas = Canvas(width = w, height = h, background= f'#{2**24 - 13 * 2**9:06x}')
canvas.pack()

class C:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def __mul__(self, other):
        return C(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)

    def __add__(self, other):
        return C(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return C(self.r - other.r, self.i - other.i)

    def __abs__(self):
        return math.sqrt(self.r**2 + self.i**2)

    def __str__(self):
        return f"{self.r} + {self.i}i"
    
def mandelbrot_set(depth, xstart = -2, xrange = 2.5, ystart = -1.25, yrange = 2.5):
    for i in range(w):
        for j in range(h + 1):
            ot = C(xrange * i / w + xstart, yrange * j / h + ystart)
            zn = C(0, 0)
            f = 1
            mp = dict()
            for n in range(1, depth + 1):
                zn = zn * zn + ot
                key = 1201 * zn.r + zn.i
                if (key in mp):
                    f = depth + 1
                    break
                if abs(zn) > 2:
                    break
                mp[key] = 1
                f += 1
            if f == depth + 1:
                canvas.create_rectangle(i, j, i + 1, j + 1)
            else:
                colour = ((f+2)**7) % (2**24)
                canvas.create_rectangle(i, j, i + 1, j + 1, outline = f'#{colour:06x}')

mandelbrot_set(30, -2, 2.5, -1.25, 2.5)
print(time.time())
canvas.mainloop()