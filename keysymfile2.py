# -*- coding: utf-8 -*-
from Tkinter import *
tk = Tk()
tv = StringVar()
Label(tk,
	  textvariable=tv,
	  relief="groove",
	  borderwidth=3,
	  font=("Courier", 20, "bold"),
	  justify=LEFT,
	  width=50,
	  padx=10,
	  pady=20,
	  takefocus=False,
	  ).pack()
Entry(tk,
	  textvariable=tv,
	  takefocus=True,
	  ).pack()
tv.set("123")
tk.mainloop()
