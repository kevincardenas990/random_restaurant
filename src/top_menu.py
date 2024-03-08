import tkinter as tk
from tkinter import ttk
from constants import WIDTH, FONT, GENRE, PLACES


class Top_Menu(tk.Menu):
    def __init__(self, window) -> FONT:
        tk.Menu.__init__(self, window)
        self.window = window
        self.initialize_menu()

    def initialize_menu(self):
        self.file_menu = tk.Menu(self, tearoff=0)
        self.file_menu=tk.Menu(self, tearoff=0) #Creates the actual dropdown
        self.file_menu.add_command(label="Open File", command=exit)
        self.file_menu.add_command(label="Save As", command=exit)
        self.file_menu.add_separator() #Seperates the commands
        self.file_menu.add_command(label="Exit", command=exit)
        self.add_cascade(menu=self.file_menu, label="File")#Links dropdown
        
        self.window.config(menu=self) #adds to windows


if __name__ == "__main__":
    window = tk.Tk()
    menu = Top_Menu(window)
    window.mainloop()