from tkinter import *
import pandas
import random
import os.path
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn = ""
#Button functions

def known_card():
    global words_to_learn
    words_to_learn.remove(current_card)
    save_words_to_learn = pandas.DataFrame(words_to_learn)
    save_words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    print(words_to_learn)
    current_card = random.choice(words_to_learn)
    print("cock")
    french_word = current_card['French']
    canvas.itemconfig(canvas_card_side, image=flashcard_front)
    canvas.itemconfig(canvas_curr_language, text="French", fill="black")
    canvas.itemconfig(canvas_curr_word, text=f"{french_word}", fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    english_word = current_card['English']
    canvas.itemconfig(canvas_card_side, image=flashcard_back)
    canvas.itemconfig(canvas_curr_language, text="English", fill="white")
    canvas.itemconfig(canvas_curr_word, text=f"{english_word}", fill="white")

#CSV work
if os.path.isfile("data/words_to_learn.csv"):
    words_to_learn = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
else:
    words_to_learn = pandas.DataFrame(pandas.read_csv("data/french_words.csv"))
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    words_to_learn = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")

# UI
window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")

canvas_card_side = canvas.create_image(400,263, image=flashcard_front)
canvas_curr_language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas_curr_word = canvas.create_text(400, 264, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
known_button = Button(image=right_img, highlightthickness=0, command=known_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
