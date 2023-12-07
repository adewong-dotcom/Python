import tkinter as tk
from PIL import Image, ImageTk
import time
import math

#Color palette
DARK_PURPLE = '#221f32'
MUSTARD = '#f8c00b'
LIGHT_YELLOW= "#f7d87b"
LIGHT_GREEN = "#1eb263"
PINK = "#f99898"
LIGHT_BLUE = "#62a7f9"
CHECK = "✔"

#Font
FONT_NAME = 'Courier'
ATTRIBUTE_FONT = ("Arial", 8, "normal")

#Timing
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#Global variables
counter = 0
num_checks = ""
reset = False
timer = None

def reset():
    global num_checks
    global counter
    global reset
    global timer
    window.after_cancel(timer)
    counter = 0
    num_checks = ""
    title['text'] = "Timer"
    title['fg'] = LIGHT_YELLOW
    canvas.itemconfig(timer_text, text="00:00")

def timer_start():
    global counter
    counter += 1

    if counter%2 != 0:
        title['text'] = "Work"
        title['fg'] = LIGHT_GREEN
        count_down(WORK_MIN * 60)
    elif counter%8 == 0:
        title['text'] = "Break"
        title['fg'] = PINK
        count_down(LONG_BREAK_MIN * 60)
    else:
        title['text'] = "Break"
        title['fg'] = LIGHT_YELLOW
        count_down(SHORT_BREAK_MIN * 60)


def count_down(count):
    global num_checks
    global counter
    global timer
    #Variables for min and seconds
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        if counter%2 == 0:
            num_checks += CHECK
            checkmarks.config(text=f"{num_checks}")


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=75, pady=75)
window['bg'] = DARK_PURPLE

title = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=LIGHT_BLUE, bg=DARK_PURPLE)
title.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=204, bg=DARK_PURPLE, highlightthickness=0)
# tomato_img = tk.PhotoImage(file="Pomodoro/tomato.png")
img = (Image.open("Pomodoro/tomato.png"))
resized_image = img.resize((200, 204))
new_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(98, 102, image=new_image)
timer_text = canvas.create_text(98, 122, text="00:00", fill=MUSTARD, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = tk.Button(window, text="Start", command=timer_start, bg=LIGHT_GREEN)
button_start.grid(column=0, row=2)

button_reset = tk.Button(window, text="Reset", command=reset, bg=LIGHT_BLUE)
button_reset.grid(column=2, row=2)

checkmarks=tk.Label(text="", fg=LIGHT_GREEN, bg=DARK_PURPLE)
checkmarks.grid(column=1, row=3)


attribute = tk.Label(text='Image by bakar015 on Freepik')
attribute_link =tk.Label(text="https://www.freepik.com/free-vector/coloured-tomato-design_938844.htm#query=tomato%20cartoon&position=9&from_view=keyword&track=ais&uuid=ddedbbdf-c583-4bf2-80e9-ffefa4278d79")
# attribute.pack()
# attribute_link.pack()

window.mainloop()