import datetime
import tkinter as tk
import random
import webbrowser
from PIL import ImageTk
from PIL import Image
import PIL.ImageTk
from time import sleep
from tkinter import *

window = tk.Tk()
window.geometry("700x700")
window.title("Go Corona Go!!!!")

image = PIL.Image.open("/Users/theshaikasad/Desktop/maxresdefault.jpg")
image.thumbnail((250, 250), PIL.Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)


year_label = tk.Label(text="Year: ")
year_label.grid(column=0, row=1)

month_label = tk.Label(text="Month: ")
month_label.grid(column=0, row=2)

day_label = tk.Label(text="Day: ")
day_label.grid(column=0, row=3)

name_label = tk.Label(text="Name: ")
name_label.grid(column=0, row=4)

year_entry = tk.Entry()
year_entry.grid(column=1, row=1)

month_entry = tk.Entry()
month_entry.grid(column=1, row=2)

day_entry = tk.Entry()
day_entry.grid(column=1, row=3)

name_entry = tk.Entry()
name_entry.grid(column=1, row=4)

calculate_now_button = tk.Button(text="Calculate now!!!!")
calculate_now_button.grid(column=1, row=5)

text23 = tk.Label(text="\nTHE SOLUTION: \n\n")
text23.grid(column=0, row=9)

img = PIL.Image.open("/Users/theshaikasad/Desktop/APLClwr_.jpg")
img.thumbnail((130, 130), PIL.Image.ANTIALIAS)
poto = ImageTk.PhotoImage(img)
label_img = tk.Label(image=poto)
label_img.grid(column=1, row=10)

corona_button = tk.Button(text="#1 solution for protection from the COVID-19!!!")
corona_button.grid(column=1, row=11)


def indication(event):
    user = Person(str(name_entry.get()), datetime.date(int(year_entry.get()),
                                            int(month_entry.get()),
                                            int(day_entry.get())))
    precise = str(datetime.date.today() - user.birthdate)
    index1 = str(precise).index(',')-1
    precise = precise[:index1]
    text_label = tk.Label(text="Yo {}, your age is {} that means {}s of your life are gone".format(user.name, user.age, precise))
    text_label.grid(column=1, row=6)

    text1 = tk.Label(text="A Deep Realization that life is finite: ")
    text1 = text1.grid(column=1, row=7)

    im = PIL.Image.open("/Users/theshaikasad/Desktop/VBu_t7ZIRVlWELIQ.jpg")
    im.thumbnail((100, 100))
    ph = ImageTk.PhotoImage(im)
    label_im = tk.Label(image=ph)
    label_im.image = ph
    label_im.grid(column=1, row=8)


def corona_sol(event):
    webbrowser.open_new_tab("https://youtu.be/cspF9QK5FlA")

corona_button.bind("<Button-1>", corona_sol)
calculate_now_button.bind("<Button-1>", indication)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        self.age = self.findAge()

    def findAge(self):
        s = (datetime.date.today() - self.birthdate)
        s = str(s//360)
        s = s[:2]
        return int(s)

swamu = Person('Swami', datetime.date(2004, 11, 13))

window.mainloop()
