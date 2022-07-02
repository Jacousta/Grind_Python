from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
global random_french

def next_word():
    data_csv = read_csv("french_words.csv")
    data_dict = data_csv.to_dict()
    global random_french
    random_french = (random.choice(data_dict['French']))
    word_label.config(text=f"{random_french}")


def flip():
    flip_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
    flip_canvas.create_image(400, 263, image=back_image)
    flip_canvas.grid(row=1, column=1, columnspan=2)
    flip_title_label = Label(text="ENGLISH", font=("arial", 50, "italic")
                             , fg="white", bg="#9CC1B0", highlightthickness=0)
    flip_title_label.place(x=340, y=140)

    flip_word_label = Label(text="WORD", font=("arial", 60, "bold"), fg="white"
                            , bg="#9CC1B0", highlightthickness=0)
    flip_word_label.place(x=330, y=230)
    data_csv = read_csv("french_words.csv")
    data_dict = data_csv.to_dict()
    if random_french in data_dict["French"]:
        print(data_dict["English"])


# ----------------------- UI Setup -----------------------#
window = Tk()
window.title("Flashy")
window.config(pady=30, padx=30, bg=BACKGROUND_COLOR)

back_image = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=img)
canvas.create_text(400, 150, text="", font=("arial", 50, "italic"))
canvas.grid(row=1, column=1, columnspan=2)

title_label = Label(text="french", font=("arial", 50, "italic")
                    , fg="black", bg="white", highlightthickness=0)
title_label.place(x=340, y=140)

word_label = Label(text="WORD", font=("arial", 60, "bold"), fg="black"
                   , bg="white", highlightthickness=0)
word_label.place(x=330, y=230)

img_right = PhotoImage(file="./images/right.png")
right_button = Button(width=100, height=100, highlightthickness=0,
                      bg=BACKGROUND_COLOR, image=img_right, command=next_word)
right_button.grid(row=2, column=2)

img_wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(width=100, height=100, highlightthickness=0,
                      bg=BACKGROUND_COLOR, image=img_wrong, command=next_word)
wrong_button.grid(row=2, column=1)

window.after(5000, flip)
window.mainloop()
