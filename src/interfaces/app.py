import tkinter as tk
from src.interfaces.home import HomePage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi Page App")
        self.geometry("400x300")

        # Container to stack frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (HomePage, HomePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

