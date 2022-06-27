# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#323232"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, timer
    window.after_cancel(timer)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps = reps + 1
    if reps % 8 == 0:
        timer_label.config(text="BREAK", fg=RED, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
        count_down(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        timer_label.config(text="BREAK", fg=PINK, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
        count_down(SHORT_BREAK_MIN)
    else:
        timer_label.config(text="WORK", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
        count_down(WORK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(thing):
    count_min = int(thing / 60)
    count_sec = thing % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfigure(canvas_text, text=f"{count_min}:{count_sec}")
    if thing > 0:
        global timer
        timer = window.after(1000, count_down, thing - 1)
    else:
        start_timer()
        checkmark = ""
        for n in range(int(reps / 2)):
            checkmark = checkmark + "✔︎"
            progress_label.config(text=checkmark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=1, column=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="End", bg=YELLOW, highlightthickness=0, command=reset)
reset_button.grid(row=3, column=3)

progress_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
progress_label.grid(row=3, column=2)

window.mainloop()
