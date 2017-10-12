#!/usr/bin/python
from tkinter import *

fr = Frame()
fr.pack()

d = {"Sam": 123, "Linda": 456, "Paulman": 563, "Cay": 789, "Horstmann": 6174, "Cornell": 234, "Ranjan": 2788,
     "Sandy": 234}

l1 = Label(fr, text="Name")
l1.pack(side='top')
e1 = Entry(fr)
e1.pack(side='top')

l2 = Label(fr, text="phone")
l2.pack(side='top')
e2 = Entry(fr)
e2.pack(side='top')


def h1():
    global e1, e2
    lst.insert('end', e1.get())
    lst.insert('end', e2.get())


def h3():
    e1.delete(0, 'end')
    e2.delete(0, 'end')


def h5(event):
    label = lst.get(ACTIVE)  # on list click
    print(label)
    ph = d.get(label)
    e1.config(text=label)
    e2.config(text=ph)


b1 = Button(fr, text="add", command=h1)
b3 = Button(fr, text="delete", command=h3)
b1.pack(side='top')
b3.pack(side='top')
'''b4=Button(fr,text="load",command=h4)
b4.pack(side='left')'''

lst = Listbox(fr)
scrll = Scrollbar(fr)
scrll.config(command=lst.yview)
lst.config(yscrollcommand=scrll.set)
scrll.pack(side='right')
lst.pack(side='left')
lst.bind('<Double-1>', h5)

for k, v in d.items():
    lst.insert('end', k)
    lst.insert('end', v)

fr.mainloop()