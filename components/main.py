from random import choice
from tkinter import *
from tkinter import messagebox

import pandas
from django.template.defaultfilters import title

BACKGROUND_COLOR = "#B1DDC6"
data=pandas.read_csv("french_words.csv")
data_dict=data.to_dict(orient="records")
random_word={}

def right_btn_clicked():#remove that word from the dict
    data_dict.remove(random_word)
    on_btn_clicked()


def on_btn_clicked():
    global random_word,flip_timer
    win.after_cancel(flip_timer)
    random_word=choice(data_dict)
    can.itemconfig(can_image,image=front_img)
    can.itemconfig(card_title,text="French",fill="black" )
    can.itemconfig(card_word,text=random_word["French"], fill="black")
    flip_timer=win.after(3000, func=flip_card)


def flip_card():
    can.itemconfig(card_title, text="English", fill="white")
    can.itemconfig(card_word, text=random_word["English"], fill="white")
    can.itemconfig(can_image,image=back_img)


win=Tk()
win.title("Flashy")
win.config(pady=50,padx=50,bg=BACKGROUND_COLOR)


can=Canvas(width=800,height=526, highlightthickness=0)

front_img=PhotoImage(file="card_front.png")
back_img=PhotoImage(file="card_back.png")#For backside to flash English words
can_image=can.create_image(400,263,image=front_img)

can.config(bg=BACKGROUND_COLOR)
card_title=can.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word=can.create_text(400,263,text="Word",font=("Arial",68,"bold"))
can.grid(row=0,column=0,columnspan=2)

btn_wrong_image = PhotoImage(file="wrong.png")
btn_wrong = Button(image=btn_wrong_image, highlightthickness=0, command=on_btn_clicked)
btn_wrong.grid(row=1,column=0)

btn_right_image = PhotoImage(file="right.png")
btn_right = Button(image=btn_right_image, highlightthickness=0, command=right_btn_clicked)
btn_right.grid(row=1,column=1)

def on_click_help():
    messagebox.showinfo(title="Help",message="Guess the English meaning for the flashed French Card.\n"
                                             "After 3 seconds, the English meaning of the French word will be flashed.\n"
                                             "Click cross button if you guessed it wrong.\n"
                                             "Click check button if you guessed it right and it'll be removed from the flash cards.\n"
                                             "\n\nCreated by Hari Ravendran.")

instructions = Button(text="Help",highlightthickness=0,command=on_click_help)
instructions.grid(row=2,column=0,columnspan=2)

flip_timer=win.after(3000,func=flip_card)

on_btn_clicked()
win.mainloop()


