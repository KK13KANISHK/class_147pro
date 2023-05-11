# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:31:58 2023

@author: kanis
"""

from tkinter import * 

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background='snow')

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label = Label(root, text="name_in_ascii: ", bg="light yellow", fg="black")

label_2 = Label(root, text="name_in_encripted_format: ", bg="green", fg="white")

def asciiConverter():
    input_word = str(enter_word.get())
    
    for letter in input_word:
        label["text"] += str(ord(letter)) + " "
        ascii= int(ord(letter))
        encripted=ascii - 1
        label_2["text"] +=  str(chr(encripted))

btn = Button(root, text="Show name in Ascii", command=asciiConverter, bg='gold', fg='black')
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label.place(relx=0.5, rely=0.7, anchor=CENTER)

label_2.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
