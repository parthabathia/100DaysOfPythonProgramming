from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
current_card = {}


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    if len(data) == 0:
        all_complete()
    else:
        current_card = random.choice(data)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(flash_image, image=card_front)
        timer = window.after(3000, flip_card)


def is_right():
    data.remove(current_card)
    new_data = pd.DataFrame(data)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(flash_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def all_complete():
    canvas.itemconfig(flash_image, image=card_front)
    canvas.itemconfig(card_title, text="All words completed.", fill="black")
    canvas.itemconfig(card_word, text="Congratulations!", fill="black")
    window.after(5000, close_window)


def close_window():
    window.destroy()


try:
    data_set = pd.read_csv("./data/words_to_learn.csv")
    if len(data_set) == 0:
        raise Exception
except FileNotFoundError:
    data_set = pd.read_csv("./data/french_words.csv")
    data = data_set.to_dict(orient="records")
except Exception:
    data_set = pd.read_csv("./data/french_words.csv")
    data = data_set.to_dict(orient="records")
else:
    data = data_set.to_dict(orient="records")

window = Tk()
window.title("French Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526)
flash_image = canvas.create_image(400, 263)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(column=1, row=1, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, command=is_right, highlightthickness=0)
right_button.grid(column=2, row=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card, highlightthickness=0)
wrong_button.grid(column=1, row=2)

next_card()

window.mainloop()
