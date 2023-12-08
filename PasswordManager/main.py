import tkinter as tk
from PIL import Image, ImageTk
from tkmacosx import Button

#Color palette
WHITE = "#FFFFFF"
DARK_BLUE = "#293040"
LIGHT_GREEN = "#87C22C"
LIGHT_BLUE = "#1C86DF"

def password_saver():
    with open("PasswordManager/pwdata.txt") as file:
        file.write(f"{website_entry} | {email_entry} | {password_entry}")
    

window = tk.Tk()
window.title("MyPass Manager")
window.config(padx=75, pady=75, bg=WHITE)

canvas = tk.Canvas(width=350, height=350, bg=WHITE, highlightthickness=0)
img = Image.open("PasswordManager/MyPass.png")
img = img.resize((350, 350))
new_img = ImageTk.PhotoImage(img)
canvas.create_image(175, 175, image=new_img)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:", bg=WHITE, fg= DARK_BLUE)
website_label.grid(row=1, column=0)
website_entry = tk.Entry(bg=WHITE, highlightthickness= 0)
website_entry.grid(row=1, column=1)

email_label = tk.Label(text="Email/ Username:", bg=WHITE, fg= DARK_BLUE)
email_label.grid(row=2, column=0)
email_entry = tk.Entry(bg=WHITE, highlightthickness=0)
email_entry.grid(row=2, column=1)

password_label = tk.Label(text="Password:", bg=WHITE, fg= DARK_BLUE)
password_label.grid(row=3, column=0)
password_entry = tk.Entry(bg=WHITE, highlightthickness=0)
password_entry.grid(row=3, column=1)
password_generate_btn = Button(window, text="Generate Password", bg=LIGHT_BLUE, fg = WHITE, highlightthickness=0, highlightbackground = "blue")
password_generate_btn.grid(row=3, column=2)

border = tk.LabelFrame(window, bd = 2, bg = "green")
add_btn = Button(window, text="Add", bg=LIGHT_GREEN, fg = WHITE, highlightthickness=0, highlightbackground = "green", command=password_saver)
add_btn.grid(row=4, column=1, rowspan=2, sticky="ew")

window.mainloop()
