# -*- coding: utf-8 -*-
import Tkinter, Image, ImageTk
FILENAME = "13.jpg"
tk = Tkinter.Tk()
c = Tkinter.Canvas(tk, width=128, height=128)
src_image = Image.open(FILENAME)

img = ImageTk.PhotoImage(src_image)
c.create_image(0, 0, image=img, anchor="nw")
c.pack()
Tkinter.Label(tk, text=FILENAME).pack()
tk.mainloop()