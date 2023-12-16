import tkinter as tk
from PIL import Image, ImageTk
import os
from password import Password
import pandas as pd
from tkinter import messagebox
from tkinter import simpledialog
from cipher import Cipher

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
filename = 'PasswordManager/pwdata.csv'
header = ['Website', 'User', 'Password']

try:
    data_df = pd.read_csv(filename)

except (pd.errors.EmptyDataError, FileNotFoundError):
    data_df = pd.DataFrame(columns = header)

if data_df.empty:
   common_user = ''

else: 
    user_counts = data_df["User"].value_counts().reset_index()
    user_counts.columns = ["User", "Count"]
    common_user = user_counts.User[user_counts.Count == user_counts.Count.max()].max()

def clear_entry(widget):
    widget.delete(0, 'end')

def get_password():
    shift = simpledialog.askinteger("Decoder", "What is the shift to decrypt?")
    website = website_entry.get()
    user = email_entry.get()
    try:
        registered_record = data_df[(data_df.User == user) & (data_df.Website == website)]
        if registered_record.empty:
            messagebox.showinfo(title="Invalid User/ Email", message="Enter a valid user/ email.")
        else:
            registered_password = registered_record.Password.to_string(index=False)
            decrypted_password = Cipher(registered_password)
            messagebox.showinfo(title="Registered Information", message=f"Website: {website}\nEmail/User: {user}\nPassword: {decrypted_password.decoder(shift)} ")
            clear_entry(password_entry)
            clear_entry(website_entry)
    except KeyError:
        messagebox.showinfo(title="Invalid User/ Email", message="Enter a valid user/ email.")

def autocomplete_user(event):
    website = website_entry.get()
    try:
        registered_user = data_df[(data_df.Website == website)].User
        if registered_user.empty:
            pass
        elif email_entry == registered_user.to_string(index=False):
            pass
        else:
            registered_user = registered_user.to_string(index=False)
            clear_entry(email_entry)
            email_entry.insert(0, registered_user)
    except KeyError:
        print("in autocomplete_user exception")
        pass

def password_adder():
    global data_df
    password.set_password()

    website = website_entry.get()
    email_user = email_entry.get()
    password_value = password.password
    index = len(data_df.index)

    if not password.verify:
        messagebox.showinfo(title="Invalid Password", message="Password should have:\n-at least 8 characters\n-2 letter characters\n-2 symbol characters")
    elif len(email_user) < 4:
        messagebox.showinfo(title="Invalid User/ Email", message="Enter a valid user/ email.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Do you want to save?\n Email/User: {email_user}\nPassword: {password_value} ")
        if is_ok:
            shift = simpledialog.askinteger("Encoder", "What is the shift to encrypt?")
            encrypted_password = Cipher(password_value)
            new_row =[website, email_user, encrypted_password.encoder(shift)]
            data_df.loc[index] = new_row
            clear_entry(website_entry)
            clear_entry(password_entry)
    
def password_saver():
    global filename
    print("saving...")
    data_df.to_csv(filename, index=False)
    window.destroy()

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
website_entry = tk.Entry(bg=WHITE, highlightthickness= 0, width=20, fg=BLACK)
website_entry.grid(row=1, column=1, pady=5)
website_entry.focus()
website_get_btn = Button(window, text="Get Password", bg=LIGHT_BLUE, fg = WHITE, highlightthickness=0, highlightbackground = "blue", command = get_password)
website_get_btn.grid(row=1, column=2, pady= 5)

email_label = tk.Label(text="Email/ Username:", bg=WHITE, fg= DARK_BLUE)
email_label.grid(row=2, column=0)
email_entry = tk.Entry(bg=WHITE, highlightthickness=0, width=40, fg=BLACK)
email_entry.grid(row=2, column=1, columnspan=2, pady= 5)
email_entry.bind("<FocusIn>", autocomplete_user)
email_entry.insert(0, common_user)


password_label = tk.Label(text="Password:", bg=WHITE, fg= DARK_BLUE)
password_label.grid(row=3, column=0)
password_entry = tk.Entry(bg=WHITE, highlightthickness=0, width=20, fg=BLACK)
password_entry.grid(row=3, column=1, pady= 5)
password = Password(password_entry)
# password_entry.bind("<FocusIn>", autocomplete_password)
password_generate_btn = Button(window, text="Generate Password", bg=LIGHT_BLUE, fg = WHITE, highlightthickness=0, highlightbackground = "blue", command = password.generator)
password_generate_btn.grid(row=3, column=2, pady= 5)

add_btn = Button(window, text="Add", bg=LIGHT_GREEN, fg = WHITE, highlightthickness=0, highlightbackground = "green", command=password_adder, width = BTN_WIDTH)
add_btn.grid(row=4, column=1, columnspan=2)

window.protocol('WM_DELETE_WINDOW', password_saver)
window.mainloop()
