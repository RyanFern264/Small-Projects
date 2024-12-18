from tkinter import *
import time
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
def timer():
    t = 0
    while t<6:
        mins, secs = divmod(t, 60)
        curr_time = '{:02d}:{:02d}'.format(mins, secs)
        print(curr_time)
        canvas.itemconfig(timer_text_canvas, text=curr_time)
        time.sleep(1)
        t += 1
        window.after(1000, timer)
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