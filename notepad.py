import tkinter
from tkinter import *

note = Tk()
note.title("NotePad")
note.geometry("1000x500")
frame = Frame(note)
frame.pack(pady=5, padx=0)

text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)

text = Text(frame, width=120, height=40, font=("calibri", 12), selectbackground="black", undo=True, yscrollcommand=text_scroll.set)
text.pack()

text_scroll.config(command=text.yview)
note.mainloop()