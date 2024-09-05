from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
# define colors, fonts, work time, breaks
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0  # representing the number of times the timer runs
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)  # cancel the current timer
    canvas.itemconfig(timer_text, text="00:00")  # return the txt in timer
    title_label.config(text="Timer", fg=GREEN)  # change the title to "Timer"
    check_mark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:  # for the reps=8
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)  # change the title to "Break" in red

    elif reps % 2 == 0:  # for reps= 2 / 4 / 6
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)  # change the title to "Break" in pink
    else:  # # for reps= 1 / 3 / 5 / 7
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)  # the number before the "."
    count_sec = count % 60  # the remainder
    if count_sec < 10:  # if it's a single digit, add a "0"
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = " "
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Create a main window:
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create a canvas widget to put the tomato img on:
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # half from the width and height
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Create a title label to show if it's a brake or timer:
title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Create a label to show the check marks under the tomato timer
check_mark_label = Label(font="bold", fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)
# Crate 2 buttons -> start, reset
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

if __name__ == '__main__':
    window.mainloop()
