"""Holds right part of GUI Pass it the master frame """

import tkinter as tk
from tkinter import ttk
from constants import WIDTH, FONT, GENRE  
from datacontroller import DC

class Right_GUI(tk.Frame):
    '''Holds the checkboxes and Genres'''
    def __init__(self, master:tk.Tk, genre, DC:DC):
        tk.Frame.__init__(self, master)
        # super().__init__("DC")
        self.genre = genre
        self.DC = DC
        self.initialize_right_gui()
    

    def initialize_right_gui(self):
        self.new_genre = tk.Entry(self)

        #Get data controllers vals 
        self.check_box_value= self.DC.check_box_value

        #Initializes ALL and GENRE's
        self._right_side_ele=[tk.Checkbutton(self,onvalue= 'all',text= 'All',variable=self.check_box_value, command=self.check_box_on_click)]
        self._right_side_ele.extend([tk.Checkbutton(self, onvalue= i ,text= self.genre[i] ,variable=self.check_box_value, command=self.check_box_on_click) for i in self.genre])
        
        self._right_side_ele.extend([
            tk.Label(self, font=FONT, width=WIDTH, text="New Genre",),
            self.new_genre,
            tk.Button(self, font=FONT, width=WIDTH, text="Add Genre",command=self.add_genre),

            ])


    def load_gui(self):
        for idx, ele in enumerate(self._right_side_ele):
            ele.grid(row=idx, column=2, sticky="w",padx=10)

    def add_genre(self):
        pass
    
    
    def check_box_on_click(self):
        self.DC.display_by_genre()
        # obj.display_by_genre()

    
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
    genres = read_txt(GENRE, True)
    dc = DC()

    gui=Right_GUI(mas, genres, dc)
    gui.load_gui()
    gui.pack()


    mas.pack()
    window.mainloop()