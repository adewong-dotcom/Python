import tkinter as tk

FONT = ("Arial", 24, "normal")

window = tk.Tk()
window.title("Ounces to Cups Converter")
window.minsize(width=500, height=300)

ounces_label = tk.Label(text="Ounces")
ounces_label["font"] = FONT
ounces_label.grid(row=0, column=0)
ounces_entry = tk.Entry()
ounces_entry.grid(row =1, column=2)

cups_label = tk.Label(text="Cups")
cups_label.config(font=FONT)
cups_label.grid(row=2, column=0)
cups_conversion = tk.Label(text="0")
cups_conversion.config(font=FONT)
cups_conversion.grid(row=3, column=2)


def oz_to_cups():
    conversion = float(ounces_entry.get()) * 0.12009504
    cups_conversion["text"] = str(conversion)

button = tk.Button(text="Convert", command=oz_to_cups)
button.grid(row=4, column=3)