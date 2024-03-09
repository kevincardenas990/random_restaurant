'''
TODO
Get Google api stoof working 
Display it to our thing.
Sort by ratings/distance
'''

from food import Food
import tkinter as tk
from tkinter import Checkbutton, ttk, messagebox 
from constants import PLACES, GENRE, START_PLACE
from google_maps import G_Directions


WIDTH =20
FONT =None

class App(Food, tk.Tk,):# Gdirections):
    def __init__(self,  screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        tk.Tk.__init__(self, screenName, baseName, className, useTk, sync, use)
        super().__init__('Food')
        self.geometry("1000x1000")
        self.title("Random Food Picker")
        self.configure(bg="light blue")
        
        #Initalize Gdirectiopns as gmap
        # self.goog = Gdirections()
        
        #Initalize Menu Bar
        self.menu_bar = tk.Menu(self)
        
        #Menu dropdown
        self.file_menu=tk.Menu(self.menu_bar, tearoff=0) #Creates the actual dropdown
        self.file_menu.add_command(label="Open File", command=exit)
        self.file_menu.add_command(label="Save As", command=exit)
        self.file_menu.add_separator() #Seperates the commands
        self.file_menu.add_command(label="Exit", command=exit)
        self.menu_bar.add_cascade(menu=self.file_menu, label="File")#Links dropdown

        self.config(menu=self.menu_bar) #adds to windows

        #Configure Master Frame
        self.master_frame=tk.Frame(self)
        self.master_frame.columnconfigure(0, weight=1, pad=200) #controls how much a column will take up space
        self.master_frame.columnconfigure(1, weight=1, pad=200)
        self.master_frame.columnconfigure(2, weight=1, pad=200)

        #Initialize Left Frame
        self.left_menu_frame = tk.Frame(self.master_frame)
        self.left_menu_frame.grid(row=0, column=0,sticky="nw", padx=5, pady=0)
        
        #Initialize Middle Frame
        self.middle_menu_frame=tk.Frame(self.master_frame)
        self.middle_menu_frame.grid(row=0, column=1,sticky="n")

        #Initialize Right Frame
        self.right_menu_frame =tk.Frame(self.master_frame)
        self.right_menu_frame.grid(row=0, column=2, sticky="ne", padx=10, pady=0)

        #Initalize New Genre Combo Box
        self.combo_box_value = tk.StringVar(value="None")
        self.new_restaurants = tk.Entry(master=self.left_menu_frame, width= 15, justify= tk.CENTER, font=FONT)
        self.new_restaurant_genre = ttk.Combobox(self.left_menu_frame, state='readonly', values=[i for i in self.genre.values()], textvariable=self.combo_box_value)
        
        #Intialize Removal Combo Box
        self.removal_value =tk.StringVar(value="None")
        self.removal_choice = ttk.Combobox(self.left_menu_frame, state='readonly', values=self.all_restaurants, textvariable=self.removal_value)

        #Intialize Time
        # self.goog_time = tk.Label(self.left_menu_frame, width=WIDTH, font=FONT)

        #Initalize Left Side Eleements
        self.left_side_ele =[
            
            tk.Label(self.left_menu_frame, font=FONT,text="Enter New Restaurant Below"),
            self.new_restaurants,
            tk.Label(self.left_menu_frame, font=FONT,text="Enter Genre of Restaurant Below"),
            self.new_restaurant_genre,
            tk.Button(master=self.left_menu_frame, command=self.add_restaurant, text="Add New Restaurants", width= WIDTH, font=FONT,bg="green",fg="white"),
            ttk.Separator(self.left_menu_frame),
            ttk.Separator(self.left_menu_frame),
            tk.Button(self.left_menu_frame,width=WIDTH, font=FONT, command=self.display_by_genre, text="Display Restaurants",),
            tk.Button(self.left_menu_frame,width=WIDTH, font=FONT, command=self.randomize_restaurant, text="Randomize Restaurants",),
            ttk.Separator(self.left_menu_frame),
            tk.Button(self.left_menu_frame,width=WIDTH, font=FONT, command=self.clear_all, text="Clear",),
            ttk.Separator(self.left_menu_frame),
            self.removal_choice,
            tk.Button(self.left_menu_frame, width=WIDTH, font=FONT, command=self.remove_restaurant, text="Remove Restaurant",bg="red",fg="white"),
            # ttk.Separator(self.left_menu_frame),
            # tk.Button(self.left_menu_frame, width= WIDTH, font=FONT, command=self.display_google_info, text="Google Display", bg="blue", fg="white"),
            # self.goog_time
        ]
        

        # Initializes the labels so they can be modified later
        self.middle_label = tk.Label(self.middle_menu_frame, text="Restaurants Here:\n")
        
        #Intiialize right side Elements
        self.middle_side_ele = [tk.Label(self.middle_menu_frame, text=f"", font=FONT) for i in range(100)]
        
        #Check box value
        self.check_box_value=tk.Variable(value= "all")  #for checkboxes
        
        #New Genre Value
        self.new_genre = tk.Entry(self.right_menu_frame)

        #Check boxes
        self.right_side_ele=[tk.Checkbutton(self.right_menu_frame, onvalue= 'all' ,text= 'All' ,variable=self.check_box_value, command=self.check_box_on_click)]
        self.right_side_ele.extend([tk.Checkbutton(self.right_menu_frame, onvalue= i ,text= self.genre[i] ,variable=self.check_box_value, command=self.check_box_on_click) for i in self.genre])
        self.right_side_ele.extend([
            tk.Label(self.right_menu_frame, font=FONT, width=WIDTH, text="New Genre",),
            self.new_genre,
            tk.Button(self.right_menu_frame, font=FONT, width=WIDTH, text="Add Genre",command=self.add_genre)
            ])
        
        

        #grid left ele's
        for idx, ele in enumerate(self.left_side_ele):
            ele.grid(row=idx, column=0, sticky="ew", pady=5, padx=3)

        #grid middle ele's
        self.middle_label.grid(row=0, column=1, sticky='nw')
        for idx, ele in enumerate(self.middle_side_ele, 1):
            if idx % 2 == 0:
                ele.grid(row=idx-1, column=2, sticky="nw", pady=2)
            else:
                ele.grid(row=idx, column=1, sticky="nw", pady=2)

        #grid right ele's
        for idx, ele in enumerate(self.right_side_ele):

            ele.grid(row=idx, column=2, sticky="w",padx=10)

        #Pack master frame
        self.master_frame.pack()
        self.mainloop()


    def check_box_on_click(self):
        '''Displays on click'''
        self.display_by_genre()

    def add_restaurant(self):
        """Adds to list in correct format"""
        if self.new_restaurants.get()=="" or not self.validate_restaurants():
            messagebox.showerror("Empty Fields", "Please add a restaurant")
        elif self.combo_box_value.get()=="None":
            messagebox.showerror("Empty Fields", "Please select a Genre")
        else:
            genre_code=list(self.genre.keys())[list(self.genre.values()).index(self.new_restaurant_genre.get())]
            self.write_txt(PLACES, f"\n{genre_code}:{self.new_restaurants.get()}")
            self.update_restaurants()
        
    def add_genre(self):
        if self.validate_genre(self.new_genre.get()) and self.new_genre.get() != "":
            self.write_txt(GENRE, f"\n{self.new_genre.get()[:3]}:{self.new_genre.get()}")
        
    def remove_restaurant(self):
        '''Remove from list in corrct format'''
        idx = self.find_line_by_item(PLACES, self.removal_value.get())
        if idx:
            self.remove_line(PLACES, idx)
            self.removal_value.set("None")
            self.update_restaurants()
        else:
            messagebox.showerror("Failed To Remove", f"Failed to remove: {self.removal_value.get()}")
    
    def randomize_restaurant(self):
        '''TODO FIX SO IT IS NOT DEPENDENT'''
        self.clear_all()
        restaurant = self.get_random_restaurant(self.check_box_value.get())
        # self.goog.update_info(START_PLACE, restaurant)
        self.middle_side_ele[0].config(text=restaurant)

    def clear_all(self):
        for ele in self.middle_side_ele:
            ele.config(text="") 

    def clear_from_index(self, idx):
        for ele in self.middle_side_ele[idx+1:]:
            ele.config(text ="")

    
    def display_all(self):
        for idx, ele in enumerate(self.all_restaurants):
            self.middle_side_ele[idx].config(text = ele) 

    def display_by_genre(self):
        var = self.check_box_value.get()
        self.clear_all()
        if var =="all":
            self.display_all()
        elif var == "0":
            self.clear_all()
        else:        
            if self.dict_restaurants.get(var):
                for idx, ele in enumerate(self.dict_restaurants.get(var)):
                    self.middle_side_ele[idx].config(text=ele, fg="black")
                self.clear_from_index(idx)
                
            else:
                self.clear_all()
                self.middle_side_ele[0].config(text=f"No Restaurants: {str(self.genre[var])}", fg="red")

    def update_restaurants(self):
        self.all_restaurants = self.get_all_restaurants()
        self.dict_restaurants = self.read_txt(PLACES)
        self.display_by_genre()
        self.removal_choice.config(values=self.all_restaurants)
    
    def update_genres(self):
        self.genre = self.read_txt(GENRE,True)

    def validate_restaurants(self):
        return True
    
    def validate_genre(self, genre):
        return  genre[:3].lower() not in self.genre.keys()
            
    # def display_google_info(self):
    #     if self.goog.start is None  or self.goog.end is None:
    #         messagebox.showinfo("Select Place to go", "Please select a restaurant")
    #     else:
    #         self.clear_all()
    #         self.goog_time.config(text=f"{self.goog.get_arrival_time()}")



def main():
    window = App()


if __name__ == "__main__":
    main()