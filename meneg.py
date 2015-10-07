# -*- coding: utf-8 -*-
from Tkinter import *
tk = Tk()
frames = {}
b = {}
for fn in 1,2,3:
	f = Frame(tk, width=100, height=200, bg="white")
	f.pack(side=LEFT, fill=BOTH)
	frames[fn] = f
	for bn in 1,2,3,4:
		b[fn, bn] = Button(frames[fn], text="%s.%s" % (fn, bn))
#первая рамка
b[1, 1].pack(side=LEFT, fill=BOTH, expand=1)
b[1, 2].pack(side=LEFT, fill=BOTH, expand=1)
b[1, 3].pack(side=BOTTOM, fill=Y)
b[1, 4].pack(side=BOTTOM, fill=BOTH)
#вторая рамка
b[2, 1].grid(row=0, column=0, sticky=NW+SE)
b[2, 2].grid(row=0, column=1, sticky=NW+SE)
b[2, 3].grid(row=1, column=0, columnspan=2, sticky=NW+SE)
#третья рамка
b[3, 1].place(relx=0.1, relwidth=0.4, relheight=0.4, anchor=NW)
b[3, 2].place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.4, anchor=CENTER)
b[3, 3].place(relx=0.9, rely=0.9, relwidth=0.4, relheight=0.4, anchor=CENTER)

tk.mainloop()