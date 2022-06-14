#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
from tkinter import *
import tkinter.font as tkFont
import time
from PIL import ImageTk, Image

# CREATING TKINTER WINDOW
root = Tk(className="Typostud")
root.attributes("-fullscreen",True)
#root.geometry("1200x800")
## SETTING BACKGROUND OF THE WINDOW  ##
root.configure(bg='navy')

#giving icon to the picture
frame=Frame(root,width=600,height=400)
frame.pack()
frame.place(anchor='center',relx=0.5,rely=0.5)
img=ImageTk.PhotoImage(Image.open("pica.jpg"))
label=Label(image=img)
label.pack()


## TITLE FOR THE PROJECT="TYPING SPEED TEST" ##
title = Label(root, text="TYPING SPEED TEST", anchor=CENTER, font="Arial 40 bold", bg="SlateBlue", fg='MistyRose2', relief="solid")
title.place(x=115, y=10)

# // INPUT BOX FROM THE USER    //##
large_font = ('Verdana',45)
e = Entry(root, width='30', bg="#F2BC94", fg="black",font=large_font)
e.place(x=60, y=300)
e.focus()


# Clear ENTRY
def clearfunc():
    e.delete(0, 'end')


# CREATING RESET BUTTON
reset = Button(root, text="RESET", bg="black", fg="SeaGreen3", font="helvetica 20", padx=20, pady=10, relief=RAISED,
               command=clearfunc)
reset.place(x=90, y=380)

# DISPLAY SENTENCES
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
text = Label(root, height='5', width='30', fg='gold', bg='black', font=fontStyle, wraplength=500, anchor=CENTER,
             justify=LEFT)
text.place(x='45', y='90')
def randomTXT():
    f = open('myfile.txt').read()
    sentences = f.split('\n')
    display = random.choice(sentences)
    text.config(text=display)
randomTXT()

# CREATING SWITCH UP BUTTON-CHANGES SENTENCES TO BE TRACED ACCORFING TO YOUR LIKINGS
switch = Button(root, text="SWITCH-UP", bg='red', fg='black', font="helvetica 20", padx=10, pady=10, relief=RAISED, command=randomTXT)
switch.place(x=300, y=380)
# CALCULATE TIME TAKEN,TOTAL WORDS,SPEED
t0 = time.time()
def calculate(*args,**kwargs):
    t1 = time.time()

    st = e.get()
    w_count = len(st.split())
    mylabel = Label(root, text="TOTAL WORDS: " + str(w_count))
    mylabel.place(x=85, y=435)
    mylabel = Label(root, text="TIME TAKEN: " + str(round(t1 - t0)))
    mylabel.place(x=315, y=435)
    if (t1 - t0) >= 120:
        mylabel = Label(root, text="SPEED: POOR")
    
        mylabel.place(x=533, y=435)
    elif(t1 - t0) >= 60 and (t1 - t0) <= 120    :
        mylabel = Label(root, text="SPEED: AVERAGE")
        mylabel.place(x=533, y=435)
    else:
        mylabel = Label(root, text="SPEED: EXCELLENT")
        mylabel.place(x=533, y=435)

calculate()
text_type_btn = Button(root, text="RESULT", font="helvetica 20",bg='Violet red',padx=10, pady=10, relief=RAISED, command=calculate).place(x=550,y=380)
root.mainloop()


# In[ ]:




