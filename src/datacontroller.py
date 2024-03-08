import tkinter as tk
from constants import WIDTH, FONT, PLACES, GENRE
from food import Food


class DC():
    '''
    Make it so that each gui section 
    never holds their own values
    they all import DC's values  
    
    '''
    def __init__(self, food:Food) -> None:
        self.food = food
        self.genre = food.genre
        self.check_box_value = tk.Variable(value ="all")
        self.combo_box_value = tk.StringVar(value="None")
        self.removal_choices = self.food.all_restaurants
        self.removal_value =tk.StringVar(value="None")
        self.restaurant_name = tk.StringVar()
        self.middle_ele_vars = [tk.StringVar() for i in range(100)]


    def update_restaurants(self):
        self.food.all_restaurants = self.food.get_all_restaurants()
        self.food.dict_restaurants = self.food.read_txt(GENRE)
        self.display_by_genre()
        self.removal_choices = self.food.all_restaurants

    def clear_from_index(self, idx):
        pass

    def display_by_genre(self):
        print("DC DBG")
        var = self.check_box_value.get()
        self.clear_all()
        if var =="all":
            for idx, ele in enumerate(self.food.all_restaurants):
                self.middle_ele_vars[idx].set(ele) 

        elif var == "0":
            self.clear_all()

        else:        
            if self.food.dict_restaurants.get(var):
                for idx, ele in enumerate(self.food.dict_restaurants.get(var)):
                    self.middle_ele_vars[idx].set(ele)
                self.clear_from_index(idx)
                
            else:
                self.clear_all()
                self.middle_ele_vars[0].set(f"No Restaurants: {str(self.genre[var])}")

    def randomize_restaurant(self):
        pass  

    def clear_all(self):
        for ele in self.middle_ele_vars:
            ele.set("")