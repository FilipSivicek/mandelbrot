from tkinter import Canvas
import math
import time

w = 1200
h = 1200

c = Canvas(width = w, height = h, background= f'#{2**24 - 13*2**9:06x}')
c.pack()

class C:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __mul__(self, other):
        self.r, self.i = self.r * other.r - self.i*other.i, self.r * other.i + self.i * other.r 
        #return C(self.r * other.r - self.i*other.i, self.r * other.i + self.i * other.r) # v inych pripadoch sa viac hodi toto
    def __add__(self, other):
        self.r, self.i = self.r + other.r, self.i + other.i
        #return C(self.r + other.r, self.i + other.i) # v inych pripadoch sa viac hodi toto
    def __str__(self):
        return f"{self.r} + {self.i}i"
    def __abs__(self):
        return math.sqrt(self.r**2 + self.i**2)
    
def mandelbrot_set(depth):
    for i in range(w):
        for j in range(h//2+1):
            ot = C(4*i/w - 2, 4*j/h - 2)
            zn = C(0, 0)
            f = 1
            mp = dict()
            for n in range(1, depth+1):
                zn*zn
                zn + ot
                key = str(zn.r) + ";" + str(zn.i)
                if (key in mp):
                    f = depth+1
                    break
                if abs(zn) > 2:
                    break
                mp[key] = 1
                f += 1
            if f == depth+1:
                c.create_rectangle(i, j, i+1, j+1)
                c.create_rectangle(i, h - j, i+1, h + 1-j)
            else:
                farb = 2**24 - 13*2**9*f
                c.create_rectangle(i, j, i+1, j+1, outline = f'#{farb:06x}')
                c.create_rectangle(i, h - j, i+1, h + 1-j, outline = f'#{farb:06x}')

mandelbrot_set(160)
print(time.time())
c.mainloop()