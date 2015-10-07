# -*- coding: utf-8 -*-
from Tkinter import *
tk = Tk()
tv = StringVar()
Entry(tk,
	  textvariable=tv,
	  takefocus=True,
	  borderwidth=10,
	  ).pack()
myColor1 = "#%02X%02X%02X" % (200, 200, 20)
Entry(tk,
	  textvariable=tv,
	  takefocus=True,
	  borderwidth=10,
	  foreground=myColor1,
	  background="#0000FF",
	  highlightcolor='green',
	  highlightbackground='red',
	  ).pack()
tk_setPalette()
tv.set("123")
tk.mainloop()
