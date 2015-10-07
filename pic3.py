# -*- coding: utf-8 -*-
from Tkinter import *
from random import choice

colors = "red orange yellow green lightblue blue violet".split()
R = 50
tk = Tk()
c = Canvas(tk, width="4i", height=300, bg="white", relief=SUNKEN)
c.pack(expand=1, fill=BOTH)

def change_ball(event):
	c.coords(CURRENT, (event.x-R, event.y-R, event.x+R, event.y+R))
	c.itemconfigure(CURRENT, fill=choice(colors))
oval = c.create_oval((100-R, 100-R, 100+R, 100+R), fill="black")
c.tag_bind(oval, "<1>", change_ball)
tk.mainloop()