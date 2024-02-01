import math
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
LONG_BREAK_MIN = 10
reps = 0
CHECK_MARK = "✓"
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text=f"00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps == 8:
        timer_label.config(text="Long Break", fg=PINK)
        countdown(LONG_BREAK_MIN * 60)
        reps = 0
        check_marks.config(text="")
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=RED)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        window.attributes()
        countdown(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = int(math.floor(count // 60))
    seconds = int(count % 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        check_marks.config(text=f"{CHECK_MARK * math.floor(reps / 2)}", fg= GREEN, bg=YELLOW, font=8)


# ---------------------------- UI SETUP ------ ------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 28, "bold"), fill="white")
canvas.grid(column=2, row=2)

start_button = Button(text="Start", bg=PINK, font=(FONT_NAME, 10), command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", bg=PINK, font=(FONT_NAME, 10), command=reset_timer)
reset_button.grid(column=3, row=3)

check_marks = Label()
check_marks.grid(column=2, row=4)

window.mainloop()
