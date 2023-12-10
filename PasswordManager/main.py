import tkinter as tk
from PIL import Image, ImageTk
import os
from password import Password
import pandas as pd
import csv

if os.name == 'posix':
    from tkmacosx import Button #for macOS
    BTN_WIDTH = 370  
else:
    from tkinter import Button #for Windows
    BTN_WIDTH = 37
#Color palette
WHITE = "#FFFFFF"
DARK_BLUE = "#293040"
LIGHT_GREEN = "#87C22C"
LIGHT_BLUE = "#1C86DF"
BLACK = "#000000"
filename = 'PasswordManager\pwdata.csv'
#data_df = pd.read_csv(filename)
header = ['Website', 'User', 'Password']
new_data = []
def password_adder():
    global filename
    global new_data
    data_to_add = [website_entry.get(), email_entry.get(), password.password]
    new_data.append(data_to_add)
    with open(filename, 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        csvwriter.writerow(data_to_add)
    with open(filename, 'r') as data:
        csvreader = csv.reader(data)
        for row in csvreader:
            new_data.append(row)
        print(new_data)
    
def password_saver():
    global filename
    global new_data
    with open(filename, 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(new_data)
    #data_df.to_csv("PasswordManager\pwdata.csv")

window = tk.Tk()
window.title("MyPass Manager")
window.config(padx=75, pady=75, bg=WHITE)

canvas = tk.Canvas(width=350, height=350, bg=WHITE, highlightthickness=0)
img = Image.open("PasswordManager/MyPass.png")
img = img.resize((350, 350))
new_img = ImageTk.PhotoImage(img)
canvas.create_image(175, 175, image=new_img)
canvas.grid(row=0, column=0, columnspan=3)

website_label = tk.Label(text="Website:", bg=WHITE, fg= DARK_BLUE)
website_label.grid(row=1, column=0)
website_entry = tk.Entry(bg=WHITE, highlightthickness= 0, width=40, fg=BLACK)
website_entry.grid(row=1, column=1, columnspan= 2, pady=5)

email_label = tk.Label(text="Email/ Username:", bg=WHITE, fg= DARK_BLUE)
email_label.grid(row=2, column=0)
email_entry = tk.Entry(bg=WHITE, highlightthickness=0, width=40, fg=BLACK)
email_entry.grid(row=2, column=1, columnspan=2, pady= 5)


password_label = tk.Label(text="Password:", bg=WHITE, fg= DARK_BLUE)
password_label.grid(row=3, column=0)
password_entry = tk.Entry(bg=WHITE, highlightthickness=0, width=20, fg=BLACK)
password_entry.grid(row=3, column=1, pady= 5)
password = Password(password_entry)
password_generate_btn = Button(window, text="Generate Password", bg=LIGHT_BLUE, fg = WHITE, highlightthickness=0, highlightbackground = "blue", command = password.generator)
password_generate_btn.grid(row=3, column=2, pady= 5)

add_btn = Button(window, text="Add", bg=LIGHT_GREEN, fg = WHITE, highlightthickness=0, highlightbackground = "green", command=password_adder, width = BTN_WIDTH)
add_btn.grid(row=4, column=1, columnspan=2)

#window.protocol('WM_DELETE_WINDOW', password_saver)
window.mainloop()
