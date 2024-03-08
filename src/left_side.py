""" Holds middle part of GUI Pass it the master frame """
import tkinter as tk
from tkinter import ttk, messagebox
from constants import WIDTH, FONT, PLACES, GENRE

from datacontroller import DC
from food import Food
class Left_GUI(tk.Frame):
    def __init__(self, master:tk.Tk, DC:DC, food:Food):
        tk.Frame.__init__(self, master)
        self.all_restaurants = food.all_restaurants
        self.master = master
        self.genre = food.genre
        print(self.genre)
        self.food =food
        self.DC = DC 
        self.initialize_left_gui()
        
        

    def initialize_left_gui(self):
        self.combo_box_value = self.DC.combo_box_value
        self.restaurant_name = self.DC.restaurant_name

        self.new_restaurants = tk.Entry(master=self, width= 15, justify= tk.CENTER, font=FONT, textvariable=self.restaurant_name)
        self.new_restaurant_genre = ttk.Combobox(self, state='readonly', values=[i for i in self.genre.values()], textvariable=self.combo_box_value)
        
        self.removal_value = self.DC.removal_value
        self.removal_choice = ttk.Combobox(self, state='readonly', values=self.all_restaurants, textvariable=self.removal_value)

        self.left_side_ele =[

        tk.Label(self, font=FONT,text="Enter New Restaurant Below"),
        self.new_restaurants,
        tk.Label(self, font=FONT,text="Enter Genre of Restaurant Below"),
        self.new_restaurant_genre,
        tk.Button(master=self, command=self.add_restaurant, text="Add New Restaurants", width= WIDTH, font=FONT,bg="green",fg="white"),
        ttk.Separator(self),
        ttk.Separator(self),
        tk.Button(self,width=WIDTH, font=FONT, command=self.display_by_genre, text="Display Restaurants",),
        tk.Button(self,width=WIDTH, font=FONT, command=self.randomize_restaurant, text="Randomize Restaurants",),
        ttk.Separator(self),
        tk.Button(self,width=WIDTH, font=FONT, command=self.clear_all, text="Clear",),
        ttk.Separator(self),
        self.removal_choice,
        tk.Button(self, width=WIDTH, font=FONT, command=self.remove_restaurant, text="Remove Restaurant",bg="red",fg="white"),
        # ttk.Separator(self.left_menu_frame),
        # # tk.Button(self.left_menu_frame, width= WIDTH, font=FONT, command=self.display_google_info, text="Google Display", bg="blue", fg="white"),
        # # self.goog_time
        ]

    def load_gui(self):    
        for idx, ele in enumerate(self.left_side_ele):
            ele.grid(row=idx, column=0, sticky="ew", pady=5, padx=3)

    def add_restaurant(self):

        """Adds to list in correct format"""
        if self.new_restaurants.get()=="":
            messagebox.showerror("Empty Fields", "Please add a restaurant")
        elif self.combo_box_value.get()=="None":
            messagebox.showerror("Empty Fields", "Please select a Genre")
        else:
            genre_code=list(self.genre.keys())[list(self.genre.values()).index(self.new_restaurant_genre.get())]
            self.food.write_txt(PLACES, f"\n{genre_code}:{self.new_restaurants.get()}")
            self.DC.update_restaurants()
        

    def display_by_genre(self):
        self.DC.display_by_genre()

    def clear_all(self):
        pass

    def remove_restaurant(self):
        pass 

    def randomize_restaurant(self):
        pass 

    
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
    restaurants = read_txt(PLACES)
    genres = read_txt(GENRE, is_genre=True)

    food = Food()
    dc = DC(food)
    gui = Left_GUI(mas, dc, food)
    gui.load_gui()
    gui.pack()

    mas.pack()
    window.mainloop()

