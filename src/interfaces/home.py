import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Home Page", font=("Arial", 16)).pack(pady=20)

        tk.Button(
            self,
            text="View Product",
            command=lambda: controller.show_frame(ProductPage)
        ).pack(pady=10)

        tk.Button(
            self,
            text="Exit",
            command=controller.quit
        ).pack(pady=10)

