# -*- coding: utf-8 -*-
from Tkinter import *
import urllib
tk = Tk()
txt = Text(tk, width=64)
txt.grid(row=0, column=0, rowspan=2)
addr=Text(tk, background="white", width=64, height=1)
addr.grid(row=1, column=1)
page=Text(tk, background="white", width=64)
page.grid(row=1, column=1)

def fetch_url(event):
	click_point = "@%s, %s" % (event.x, event.y)
	trs = txt.tag_ranges("href")
	url = ""

	for i in range(0, len(trs), 2):
		if txt.compare(trs[i], "<=", trs[i+1]):
			url=txt.get(trs[i], trs[i+1])
	html_doc = urllib.urlopen(url).read()
	addr.delete("1.0", END)
	addr.insert("1.0", url)
	page.delete("1.0", END)
	page.insert("1.0", html_doc)

textfrags = ["My favorite Python site: ", "http://www.python.org", "\nJython site: ", "http://www.jython.org", "\nThe End!"]
for frag in textfrags:
	if frag.startswith("http:"):
		txt.insert(END, frag, "href")
	else:
		txt.insert(END, frag)
txt.tag_bind("href", "<1>", fetch_url)

tk.mainloop()

