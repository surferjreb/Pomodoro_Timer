import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
CHECKMARK = '✔'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def timer_reset():
    global reps
    global timer

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ----------------------------- #


def start_timer():
    global reps

    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    reps += 1
    if reps == 8:
        title_label.config(text="Break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg=PINK)
        count_down(short_break)
    elif reps % 2 > 0:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_min)


# ---------------------------- COUNTDOWN MECHANISM -------------------------- #


def count_down(count):
    global reps
    global timer

    counter_min = math.floor(count / 60)
    counter_sec = count % 60

    if counter_min < 10:
        counter_min = f"0{counter_min}"

    if counter_sec < 10:
        counter_sec = f"0{counter_sec}"

    canvas.itemconfig(timer_text, text=f"{counter_min}:{counter_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECKMARK

        check_mark.config(text=marks)

        if reps <= 8:
            window.lift()
            start_timer()
        else:
            window.lift()
            title_label.config(text="Complete!!")


# ---------------------------- UI SETUP ------------------------------- #


# Window/Frame config
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title
title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW,
                            font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)
# Canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_button = tkinter.Button(text="Start", highlightthickness=0,
                              command=start_timer)
reset_button = tkinter.Button(text="Reset", highlightthickness=0,
                              command=timer_reset)

start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)


check_mark = tkinter.Label(text="", fg=RED, bg=YELLOW,)

check_mark.grid(column=1, row=3)

window.mainloop()
