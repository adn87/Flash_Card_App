from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# UI setup
window = Tk()
window.title("Flash Card Application")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image=card_front_img)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)


# Button
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)


window.mainloop()
