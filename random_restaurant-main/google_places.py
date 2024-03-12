import requests
import json
import random
from googlesearch import search
from bs4 import BeautifulSoup
from constants import KEY, NEARBYURL, AMERICANFORK, OREM, PROVO, TESTURL, TEXTURL
from google_maps import G_Directions
# from google_photos import G_Photos


class G_Places():   

    def __init__(self, search:str="restaurant", location:str=AMERICANFORK, radius:int=20000, type ="restaurant") -> None:
        self.radius = radius #Give in meters
        self.search = search
        self.choice = None
        self.type = type
        self.location= location #Change to the initializer 
        self.URL = TEXTURL
        self.initialize_class()

    def initialize_class(self):  
        self.query_string = {
            "location": AMERICANFORK,
            "query":self.search,
            "radius":self.radius,
            "type":self.type ,
            "key":KEY
        }

        self.json = self._get_json()

        if self._validate_response():
            self.choice = random.choice(self.json["results"])
            # self.print_cadidates()
            # self.write_results()
            self._initialize_info()

    def get_photo_info(self):
        return self.json["results"][0]["photos"]

    def write_results(self):
        with open("temp.txt", 'w') as out_file:
            out_file.writelines(self.json)

    def print_cadidates(self):
        counter = 1
        for i in self.json["results"]:
            print(counter, i["name"])
            counter+=1

    def get_restaurant_rating(self):
        return self.json["results"][0]["rating"]

    def get_travel_time(self, start = "818 E 500 s AF UT"):
        if self._validate_response():
            self.GD = G_Directions("818 E 500 s AF UT", self.address)
            return self.GD.get_arrival_time()
        print("ERROR <GPLACEs TRAVEL_TIME>")

    def _get_json(self):  
        response = requests.get(self.URL, params=self.query_string) 
        return response.json() 

    def _validate_response(self):
        if len(self.json['results']) != 0:
            return True
        print("VALIDATION FAILED <GPLACES>")
        return False 

    def _initialize_info (self):
        if self._validate_response():
            self.name  = self.choice["name"]
            self.address = self.choice["geometry"]["location"]["lat"], self.choice["geometry"]["location"]["lng"]
            return
        return None



if __name__ == "__main__":
    distance = G_Places(search="fusion", radius=1000)
    print(distance.name)
    print(distance.get_travel_time())
# soup = BeautifulSoup(urllib.request.urlopen(TESTURL),"html.parser")
# print(soup.text)    





