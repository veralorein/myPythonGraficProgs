# -*- coding: utf-8 -*-
from Tkinter import *
from ScrolledText import ScrolledText

tk = Tk()
txt = ScrolledText(tk)
txt.pack()

for x in range(1, 1024):
	txt.insert(END, str(2L**x)+"\n")
tk.mainloop()