# -*- coding: utf-8 -*-
from Tkinter import *
import Image, ImageTk, tkFileDialog
global img, imgobj
import gobject
import gst

def show():
	global img, imgobj
	filename = tkFileDialog.askopenfilename()
	if filename != ():
		src_img = Image.open(filename)
		img = ImageTk.PhotoImage(src_img)
		c.itemconfigure(imgobj, image=img, anchor="nw")

tk = Tk()
main_menu = Menu(tk)
tk.config(menu=main_menu)
file_menu = Menu(main_menu)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=show)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=tk.destroy)

c = Canvas(tk, width=300, height=300, bg="white")
imgobj = c.create_image(0, 0)
c.pack()

tk.mainloop()