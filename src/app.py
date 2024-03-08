"""
TODO
Get Google api stoof working 
Display it to our thing.
Sort by ratings/distance

Idea is to split fields to left, mid, right, controller and app
"""

import tkinter as tk
from tkinter import Checkbutton, ttk, messagebox
from abc import ABC 
from constants import PLACES, GENRE, START_PLACE, WIDTH, FONT
from google_maps import Gdirections
from food import Food

from datacontroller import DC
from top_menu import Top_Menu
from right_side import Right_GUI
from left_side import Left_GUI
from mid_side import Mid_GUI

class App(tk.Tk):# Gdirections):
    def __init__(self,  screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        tk.Tk.__init__(self, screenName, baseName, className, useTk, sync, use)
        self.food =Food()
        self.all_restaurants=self.food.all_restaurants
        self.genre =self.food.genre
        self.initialize_gui()
    
    def initialize_gui(self):

        self.geometry("1000x1000")
        self.title("Random Food Picker")
        self.configure(bg="light blue")
        self.test=20

        #Initalize Menu Bar
        self.menu_bar = Top_Menu(self)
        
        #Configure Master Frame
        self.master_frame=tk.Frame(self)
        self.master_frame.columnconfigure(0, weight=1, pad=200) #controls how much a column will take up space
        self.master_frame.columnconfigure(1, weight=1, pad=200)
        self.master_frame.columnconfigure(2, weight=1, pad=200)

        #initialize Data Controller
        self.DC = DC(self.food)

        #Initialize Food


        #TODO Initialize Left Frame by calling the Class
        self.left_frame = Left_GUI(self.master_frame, self.DC, self.food)
        self.left_frame.grid(row=0, column=0,sticky="nw", padx=5, pady=0)

        #TODO Initialize Middle Frame by calling the Class
        self.middle_frame=Mid_GUI(self.master_frame, self.genre, self.DC)
        self.middle_frame.grid(row=0, column=1,sticky="n")

        #TODO Initialize Right Frame by calling the Class
        # Right_GUI.check_box_on_click = classmethod(App.check_box_on_click)
        self.right_frame = Right_GUI(self.master_frame, self.genre, self.DC)
        self.right_frame.grid(row=0, column=2, sticky="ne", padx=10, pady=0)
        
        self.left_frame.load_gui()
        self.middle_frame.load_gui()
        self.right_frame.load_gui()

        self.master_frame.pack()
        
    # def check_box_on_click(self):
    #     '''Displays on click'''
    #     print("I CLASSED ", self)
    #     self.display_by_genre()


    # def add_genre(self):
    #     if self.validate_genre(self.new_genre.get()) and self.new_genre.get() != "":
    #         self.write_txt(GENRE, f"\n{self.new_genre.get()[:3]}:{self.new_genre.get()}")
        
    # def remove_restaurant(self):
    #     '''Remove from list in corrct format'''
    #     idx = self.find_line_by_item(PLACES, self.removal_value.get())
    #     if idx:
    #         self.remove_line(PLACES, idx)
    #         self.removal_value.set("None")
    #         self.update_restaurants()
    #     else:
    #         messagebox.showerror("Failed To Remove", f"Failed to remove: {self.removal_value.get()}")
    
    # def randomize_restaurant(self):
    #     '''TODO FIX SO IT IS NOT DEPENDENT'''
    #     self.clear_all()
    #     restaurant = self.get_random_restaurant(self.check_box_value.get())
    #     # self.goog.update_info(START_PLACE, restaurant)
    #     self.middle_side_ele[0].config(text=restaurant)

    # def clear_all(self):
    #     for ele in self.middle_side_ele:
    #         ele.config(text="") 

    # def clear_from_index(self, idx):
    #     for ele in self.middle_side_ele[idx+1:]:
    #         ele.config(text ="")

    # def display_all(self):
    #     for idx, ele in enumerate(self.all_restaurants):
    #         self.middle_side_ele[idx].config(text = ele) 

    # def update_restaurants(self):
    #     self.all_restaurants = self.get_all_restaurants() #update Food
    #     self.dict_restaurants = self.read_txt(PLACES) #Update text file
    #     self.display_by_genre()# Re display values
    #     self.removal_choice.config(values=self.all_restaurants)#Update removals
    
    # def update_genres(self):
    #     self.genre = self.read_txt(GENRE,True)




def main():
    window = App()
    window.mainloop()

if __name__ == "__main__":
    main()