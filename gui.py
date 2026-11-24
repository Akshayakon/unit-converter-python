"""Simple tkinter GUI for the unit converter."""
import tkinter as tk
from tkinter import ttk

from converter import CATEGORIES

root = tk.Tk()
root.title("Unit Converter")
root.resizable(False, False)

category, value, src, dst, result = (tk.StringVar() for _ in range(5))


def update_units(*_):
    units = list(CATEGORIES[category.get()][1])
    from_box["values"] = to_box["values"] = units
    src.set(units[0])
    dst.set(units[1])
    result.set("")


def convert(*_):
    try:
        func = CATEGORIES[category.get()][0]
        out = func(float(value.get()), src.get(), dst.get())
        result.set(f"{value.get()} {src.get()} = {out:.4g} {dst.get()}")
    except ValueError:
        result.set("Please enter a valid number.")


frame = ttk.Frame(root, padding=15)
frame.grid()

ttk.Label(frame, text="Category").grid(row=0, column=0, sticky="w")
ttk.Combobox(frame, textvariable=category, values=list(CATEGORIES), state="readonly").grid(row=0, column=1, pady=3)
ttk.Label(frame, text="Value").grid(row=1, column=0, sticky="w")
ttk.Entry(frame, textvariable=value).grid(row=1, column=1, pady=3)
ttk.Label(frame, text="From").grid(row=2, column=0, sticky="w")
from_box = ttk.Combobox(frame, textvariable=src, state="readonly")
from_box.grid(row=2, column=1, pady=3)
ttk.Label(frame, text="To").grid(row=3, column=0, sticky="w")
to_box = ttk.Combobox(frame, textvariable=dst, state="readonly")
to_box.grid(row=3, column=1, pady=3)
ttk.Button(frame, text="Convert", command=convert).grid(row=4, column=0, columnspan=2, pady=8)
ttk.Label(frame, textvariable=result, font=("Segoe UI", 11, "bold")).grid(row=5, column=0, columnspan=2)

category.trace_add("write", update_units)
root.bind("<Return>", convert)
category.set("length")

root.mainloop()
