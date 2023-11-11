from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# Flash Cards
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

# UI setup
window = Tk()
window.title("Flash Card Application")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image=card_front_img)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)


# Button
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
right_button.grid(row=1, column=1)
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
