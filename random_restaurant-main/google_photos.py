import requests
import json
from constants import *
from bs4 import BeautifulSoup
from PIL import ImageTk, Image


temp_ref = 'ATplDJYdLMeNhrWAFgXo9S0pq3o4j3ud_1zQAM7DeUs9YgQamXSwLrfXUmqb-B-9pWu03JkV0Lk_xIzvtTEezJzNxx9abMgi5_JUKkiadLGUmSHZ3OLT9fya4VsJo4-195ub9bsPQ0kydOOWO6JTynVLwkzGLMLvaVBmBRQjTFZEOe9EAn-K'
temp_width = '6545'
temp_height = '4363'

class G_Photos():
    def __init__(self, photo_ref, max_height, max_width) -> None:
        self.photo_ref = photo_ref
        self.max_height = max_height
        self.max_width = max_width
        self.URL = PHOTOURL
        self.initialize_class()


    def initialize_class(self):
        self.query_string = {
            "photo_reference": self.photo_ref,
            "maxheight": self.max_height,
            "maxwidth": self.max_width,
            "key":KEY
        }
        self.json = self._get_photo() 
        
    def _validate_response(self):
        if len(self.json['results']) != 0:
            return True
        print("VALIDATION FAILED <GPLACES>")
        return False 
    
    def _format_query_string(self):
        '''NEEDS TO CHANGE to %20 for query '''
        new_query = self.URL
        for i in self.query_string.keys():
            new_query += f"&{i}={self.query_string[i]}"
        return new_query

    def _get_photo(self):  
        return requests.get(self.URL, params=self.query_string).json() 
        
    
G_Photos(temp_ref, temp_height, temp_width)
