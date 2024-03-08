import random
from constants import PLACES, GENRE

class Food():

    def __init__(self, restaurants:str= None, genre:str=None,  ) -> None:
        self.all_restaurants = self.get_all_restaurants()
        self.dict_restaurants= self.read_txt(PLACES)
        self.genre = self.read_txt(GENRE, is_genre=True)

    def find_line_by_item(self, filename, item)-> int:
        with open(filename, 'r', encoding="UTF-8") as in_file:
            for idx, ele in enumerate(in_file.readlines(), 0):
                temp = ele.strip('\n').split(':')
                if temp[1] == item:
                    return idx
            # return None
    
    def remove_line(self, filename:str, line_num)->None:        
        with open(filename, 'r+', encoding="UTF-8") as in_file:
            lines = in_file.readlines()
            in_file.seek(0)
            in_file.truncate()
            for idx, line in enumerate(lines):
                if idx != line_num:
                    if line =="":
                        continue
                    in_file.write(line)
                


    def read_txt(self, filename:str, is_genre=False ) ->dict:
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
            
    def get_all_restaurants(self):
        return [k for i  in self.read_txt(PLACES).values() for k in i]

    def write_txt(self, filename:str, item:str)->None:
        with open(filename, 'a') as out_file:
            out_file.writelines(f"{item}")

    def get_random_restaurant(self, genre)->str:
        if genre == "all":
            return random.choice(self.all_restaurants)
        else:
            return random.choice(self.dict_restaurants[genre])

Need_To_Go = [


    "Waffle Love",
    "Bam Bams BBQ",
    "Village Inn"

]

def main():
    food = Food()
    rests = food.read_txt(filename="restaurants.txt")
    print(food.all_restaurants)


if __name__ == "__main__":
    main()

