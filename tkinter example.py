import tkinter as tk

window=tk.Tk() #root window object
window.title ('TKInter hello world')

text=tk.Label(text='hello world', foreground = 'white', background = 'blue', width = 30, height = 3)
text2=tk.Label(text='hello world 2')
text3=tk.Label(text='hello world 3')

text.pack()
text2.pack()
text3.pack()

entry=tk.Entry(width=30)
entry.pack()
name = entry.get()
entry.delete(0,tk.END)

print(text.configure().keys())

window.mainloop() #start event loop, methid on top of 'window'
