# -*- coding: utf-8 -*-
from Tkinter import *
import Image, ImageTk, tkFileDialog

class App(Tk):
	def __init__(self):
		Tk.__init__(self)
		main_menu = Menu(self)
		self.config(menu=main_menu)
		file_menu = Menu(main_menu)
		main_menu.add_cascade(label="File", menu=file_menu)
		file_menu.add_command(label="Open", command=self.show_img)
		file_menu.add_separator()
		file_menu.add_command(label="Exit", command=self.destroy)

		self.c = Canvas(self, width=300, height=300, bg="white")
		self.imgobj = self.c.create_image(0, 0)
		self.c.pack()

	def show_img(self):
		filename = tkFileDialog.askopenfilename()
		if filename != ():
			src_img = Image.open(filename)
			self.img = ImageTk.PhotoImage(src_img)
			self.c.itemconfigure(self.imgobj, image=self.img, anchor="nw")

app = App()
app.mainloop()