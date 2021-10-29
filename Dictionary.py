# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 16:11:01 2021

@author: DELL
"""

from tkinter import *
import random
root=Tk()

root.title("Dictionary")

root.geometry("400x400")

label1=Label(root)
label2=Label(root)
label3=Label(root)

dictionary={
    "mutable":"Value can be changed as a list",
    "immutable":"Value cannot be changed as a tuple",
    "tkinter":"It is a GUI library of Pyhton"}

def mutable():
    label1["text"]=dictionary["mutable"]
    
def immutable():
    label1["text"]=dictionary["immutable"]

def tkinter():
    label1["text"]=dictionary["tkinter"]
    
btn1=Button(root, text="Mutable", command=mutable)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)

btn2=Button(root, text="Immutable", command=immutable)
btn2.place(relx=0.5, rely=0.6, anchor=CENTER)

btn3=Button(root, text="Tkinter", command=tkinter)
btn3.place(relx=0.5, rely=0.7, anchor=CENTER)

label1.place(relx=0.5, rely=0.4, anchor=CENTER)
label2.place(relx=0.5, rely=0.3, anchor=CENTER)
label3.place(relx=0.5, rely=0.2, anchor=CENTER)



root.mainloop()