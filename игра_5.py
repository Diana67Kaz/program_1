'''
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        if isinstance(other,Item):
            return self.price + other.price
        if isinstance(other,int):
            return self.price + other
    def __sub__(self, other):
        if isinstance(other,Item):
            return self.price-other.price
        if isinstance(other,int):
            return self.price-other
    def __mul__(self, other):
        if isinstance(other,Item):
            return self.price*other.price
        if isinstance(other,int):
            return self.price*other
    def __floordiv__(self, other):
        if isinstance(other,Item):
            return self.price//other.price
        if isinstance(other,int):
            return self.price//other

Item1 = Item('Видеокарта', 2000)
Item2 = Item('Процессор', 1000)

print(Item1+Item2)
print(Item1+50)
print(Item1-Item2)
print(Item1-50)
print(Item1*Item2)
print(Item2*2)
print(Item1//Item2)
print(Item1//2)
'''

from tkinter import *
import random

window = Tk()
window.geometry('600x600')

class Fire:
    image = PhotoImage(file='two_fire.png').subsample(4, 4)

class Water:
    image = PhotoImage(file='two_fire.png').subsample(4, 4)

class Earth:
    image = PhotoImage(file='two_fire.png').subsample(4, 4)

class Wind:
    image = PhotoImage(file='two_fire.png').subsample(4, 4)

elements = [Fire(), Earth(), Water(), Wind()]

canvas = Canvas(window, width=600, height=600)
canvas.pack()

for elem in elements:
    img = canvas.create_image(random.randint(50,550), image=elem.image)



window.mainloop()
'''