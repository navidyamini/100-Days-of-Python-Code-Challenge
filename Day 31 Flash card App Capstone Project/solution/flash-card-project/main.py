from tkinter import *
import pandas as pd
import random
FONT_NAME = "Arial"
BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
try:
    data_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_df.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas_card_front.itemconfig(title_text, text='French', fill='black')
    canvas_card_front.itemconfig(word_text, text=current_card['French'], fill='black')
    canvas_card_front.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas_card_front.itemconfig(title_text, text='English', fill='white')
    canvas_card_front.itemconfig(word_text, text=current_card['English'], fill='white')
    canvas_card_front.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Image Path
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Canvas
canvas_card_front = Canvas(width=800, height=526, highlightthickness=0)
card_background = canvas_card_front.create_image(400, 263, image=card_front_img)
canvas_card_front.grid(column=0, row=0, columnspan=2)
canvas_card_front.config(bg=BACKGROUND_COLOR)
title_text = canvas_card_front.create_text(400, 150, text="title", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas_card_front.create_text(400, 263, text="word", fill="black", font=(FONT_NAME, 60, "bold"))

# Buttons
button_right = Button(image=right_img, highlightthickness=0, command=is_known)
button_right.grid(column=1, row=1)

button_wrong = Button(image=wrong_img, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=1)
next_card()

window.mainloop()
