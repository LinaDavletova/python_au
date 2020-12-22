# HW1 Triangles

+ [Triangles](#Triangles)

## Triangles.py

```python
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + " ," + str(self.y) + ")"

    def __add__(self, other):  # длина
        length = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** (1 / 2)
        return length


class Triangle(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def p(self):
        return (self.a + self.b + self.c) / 2

    def __str__(self):
        return str(self.a) + " " + str(self.b) + " " + str(self.c)

    def area(self):
        if self.a != self.b and self.b != self.c and self.a != self.c:
            return 0
        return (self.p() * (self.p() - self.a) * (self.p() - self.b) * (self.p() - self.c)) ** (1 / 2)


fin = open('in.txt', 'r')
fout = open('out.txt', 'w')

maxarea, x1max, y1max, x2max, y2max, x3max, y3max = 0, 0, 0, 0, 0, 0, 0
for i in fin:
    try:
        if len(list(map(int, i.split(" ")))) == 6:
            x1, y1, x2, y2, x3, y3 = (list(map(int, i.split(" "))))
            a = Point(x1, y1)
            b = Point(x2, y2)
            c = Point(x3, y3)
            t = Triangle(a + b, b + c, c + a)
            if t.area() > maxarea:
                maxarea = t.area()
                x1max, y1max, x2max, y2max, x3max, y3max = x1, y1, x2, y2, x3, y3
    except ValueError:
        print("error")

if maxarea != 0:
    fout.write(
        str(x1max) + " " + str(y1max) + " " + str(x2max) + " " + str(y2max) + " " + str(x3max) + " " + str(y3max))
fout.close()
fin.close()
```

