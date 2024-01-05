from tkinter import *
import random
from PIL import Image, ImageTk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
checkmark_location = 200
sessions_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global sessions_count
    sessions_count = 0
    canvas.itemconfig(session_text, text="Begin?", fill=YELLOW)
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    canvas.itemconfig(session_text, text="FOCUS", fill=RED)
    count_down(WORK_MIN*60)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global sessions_count, checkmark_location, timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if sessions_count < 1:
        canvas.create_image(900, checkmark_location, image = checkmark)

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count >0:
        timer = window.after(1000, count_down, count-1)
    else:
        sessions_count +=1
        if sessions_count % 2 == 1 and sessions_count < 7:
            canvas.itemconfig(session_text, text="BREAK TIME", fill=YELLOW)
            count_down(SHORT_BREAK_MIN*60)
        elif sessions_count % 2 == 1 and sessions_count % 7 == 0:
            canvas.itemconfig(session_text, text="LONG BREAK", fill=GREEN)
            count_down(LONG_BREAK_MIN*60)
        elif sessions_count % 2 == 0:
            canvas.itemconfig(session_text, text="FOCUS", fill=RED)
            count_down(WORK_MIN*60)
            checkmark_location += 50
            canvas.create_image(900, checkmark_location, image = checkmark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(bg = GREEN)



original_green = Image.open("Tomatoes/green.png")
resized_green = original_green.resize(size=(60,60))

tomato_counter = random.randint(1,9)
canvas = Canvas(width = 1024, height=1024)
background = PhotoImage(file=f"Tomatoes/t{tomato_counter}.png")
checkmark = ImageTk.PhotoImage(resized_green)
canvas.create_image(512, 512, image = background)
timer_text = canvas.create_text(500, 180, text = "00:00", font=(FONT_NAME, 100, "bold"))
canvas.pack()

session_text = canvas.create_text(500, 90, text = "FOCUS", font=(FONT_NAME, 90, "bold"), fill=RED)


start_button = Button(text = "Start", font=(FONT_NAME, 30, "bold"), width = 8, height = 2, command=start_timer)
start_button.place(x=420, y=230)

reset_button = Button(text = "Reset", font=(FONT_NAME, 30, "bold"), width = 8, height = 2, command=timer_reset)
reset_button.place(x=420, y=330)


checkmark_location = 200
canvas.create_image(900, checkmark_location, image = checkmark)




window.mainloop()