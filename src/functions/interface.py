import tkinter as tk

def ProductContainer(root, name, price, qnt):
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(fill="both", expand=True)
    label_title = tk.Label(frame, text=name, font=("Arial", 10, "bold"))
    label_title.pack(anchor="w")
    label_value = tk.Label(frame, text=price, wraplength=350)
    label_value.pack(anchor="w", pady=(0, 10))
    return frame