# -*- coding: utf-8 -*-
from Tkinter import *
tk = Tk()
txt = Text(tk)
txt.pack()
#функ обработки события
def even_info(event):
	txt.delete("1.0", END)
	for k in dir(event):
		if k[0] != "_":
			ev = "%15s: %s\n" % (k, repr(getattr(event, k)))
			txt.insert(END, ev)
txt.bind("<KeyPress>", even_info)
tk.mainloop()
