""" Holds middle part of GUI Pass it the master frame """
import tkinter as tk
from tkinter import ttk
from constants import WIDTH, FONT, GENRE, PLACES
from datacontroller import DC
from food import Food

class Mid_GUI(tk.Frame):
    def __init__(self, master:tk.Tk, genre, DC:DC):
        tk.Frame.__init__(self, master)
        self.master = master
        self.DC=DC
        self.genre = genre 
        self.initialize_mid_gui()

    def initialize_mid_gui(self):
        self.middle_label = tk.Label(self, text="Restaurants Here:\n")
        self.middle_side_ele = [tk.Label(self, text=f"", font=FONT, textvariable=self.DC.middle_ele_vars[i]) for i in range(100)]

    def load_gui(self):
        self.middle_label.grid(row=0, column=1, sticky='nw')
        for idx, ele in enumerate(self.middle_side_ele, 1):
            if idx % 2 == 0:
                ele.grid(row=idx-1, column=2, sticky="nw", pady=2)
            else:
                ele.grid(row=idx, column=1, sticky="nw", pady=2)


def read_txt(filename:str, is_genre=False ) ->dict:
    items ={}
    try:
        with open(filename,'r', encoding= "UTF-8") as in_file:
            lines =in_file.readlines()
            for i in lines:
                temp = i.strip('\n').split(':')
                if temp =="":
                    continue
                if temp[0] in items.keys():
                    if is_genre:
                        continue
                    items[temp[0]].append(temp[1])
                else:
                    if is_genre:
                        items[temp[0]] = temp[1]
                        continue
                    items[temp[0]] = [temp[1]]
        return items
        
    except FileNotFoundError:
        with open(filename,'w',encoding="UTF-8") as in_file:
            return {"None":"None"}
        

if __name__ == "__main__":

    window = tk.Tk()
    window.geometry("1000x1000")
    mas = tk.Frame(window)
    genres = read_txt(GENRE, True )
    food = Food()
    dc = DC(food)

    dc.middle_ele_vars[0].set("Hello :3")
    gui=Mid_GUI(mas, genres, dc)
    gui.load_gui()
    gui.pack()

    print(dc.middle_ele_vars[0].get())


    mas.pack()
    window.mainloop()