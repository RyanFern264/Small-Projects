from tabnanny import check
from tkinter import *

from clyent import color

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 
timer_secs = 0
timer_mins = 0
def timer():
    global timer_secs
    global timer_mins
    global timer_text_canvas
    timer_secs += 1
    if timer_secs == 60:
        timer_mins += 1
    timer_text = str(timer_mins) + ":" + str(timer_secs)
    canvas.itemconfig(timer_text_canvas, text=timer_text)
     #config(text=timer_text))
    return timer_text
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
tomato_canvas = canvas.create_image(100, 112, image=tomato_img)
timer_text_canvas = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

check_marks = Label(text="✔", bg=YELLOW, highlightthickness=0, fg=GREEN)
check_marks.grid(column=2, row=4)


reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(column=3, row=3)

start_button = Button(text="Start", command=timer)
start_button.grid(column=1, row=3)


window.after(1000, timer)
window.mainloop()