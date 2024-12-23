from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"




# UI
window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
flashcard_front = PhotoImage(file="images/card_front.png")
#flashcard_back = PhotoImage(file="images/card_back.png")
#flashcard_word = canvas.create_text(400, 264, text="Word")
canvas.create_image(400,263, image=flashcard_front)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 264, text="Word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0)
unknown_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
known_button = Button(image=right_img, highlightthickness=0)
known_button.grid(row=1, column=1)

window.mainloop()
