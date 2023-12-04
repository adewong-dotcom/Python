import tkinter as tk

FONT = ("Arial", 24, "normal")

window = tk.Tk()
window.title("Ounces to Cups Converter")
window.config(padx=20, pady= 20)
# window.minsize(width=500, height=300)

ounces_entry = tk.Entry(width=7)
ounces_entry.grid(row =0, column=1)

ounces_label = tk.Label(text="Ounces")
# ounces_label["font"] = FONT
ounces_label.grid(row=0, column=2)

equals_label = tk.Label(text="is equal to")
# ounces_label["font"] = FONT
equals_label.grid(row=1, column=0)

cups_conversion = tk.Label(text="0")
cups_conversion.config(font=FONT)
cups_conversion.grid(row=1, column=1)

cups_label = tk.Label(text="Cups")
# cups_label.config(font=FONT)
cups_label.grid(row=1, column=2)


def oz_to_cups(event):
    conversion = float(ounces_entry.get()) / 8
    cups_conversion["text"] = str(conversion)


button = tk.Button(text="Convert", command=oz_to_cups)
button.grid(row=2, column=1)
window.bind('<Return>', oz_to_cups)
window.mainloop()