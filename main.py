import random
from tkinter import *
import pandas as pd
import random as rd

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# ---------------------------- UI SETUP ------------------------------- #
# since we have imported all classes, we do not need to tkinter.Tk() to access the Tk class
# first configure the window
window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

ALL_WORDS = []

def read_csv():
    df_words = pd.read_csv("data/french_words.csv")
    global ALL_WORDS
    ALL_WORDS = df_words.to_dict(orient="records")

def next_card():
    random_card = rd.choice(ALL_WORDS)
    random_fr_word = random_card["French"]
    canvas.itemconfig(txt_lang, text="French")
    canvas.itemconfig(txt_word, text=random_fr_word)


# next configure the canvas
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)

# next configure the image on the canvas
img_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=img_front)

# next add the language title
txt_lang = canvas.create_text(400,150, text="",  font=(FONT_NAME, 40, "italic"))

# next add the word in the language
txt_word = canvas.create_text(400,263, text="", font=(FONT_NAME, 60, "bold"))

# position the canvas on the grid
canvas.grid(row=0, column=0, columnspan=2)

img_right = PhotoImage(file="images/right.png")
img_wrong = PhotoImage(file="images/wrong.png")
img_back = PhotoImage(file="images/card_back.png")

# position the wrong button on the grid
btn_wrong = Button(image=img_wrong, highlightthickness=0, command=next_card)
btn_wrong.grid(row=1, column=0)

# position the right button on the grid
btn_right = Button(image=img_right, highlightthickness=0, command=next_card)

btn_right.grid(row=1, column=1)

# Read everything from the csv and write to an array
read_csv()


next_card()
















window.mainloop()