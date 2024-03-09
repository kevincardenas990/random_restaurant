from googlesearch import search
import urllib
from bs4 import BeautifulSoup
from constants import KEY, PLACESURL
import json

URL = r"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&key=AIzaSyBe33L7Etyg7QZFdEfqOyHgvuqLh2Ul0yE"
TESTURL = r"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry%2Cphotos&input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&key=AIzaSyBe33L7Etyg7QZFdEfqOyHgvuqLh2Ul0yE"

r'''
https://maps.googleapis.com/maps/api/place/findplacefromtext/json?
QUERY STRING: 
fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry%2Cphotos     #%2C is comma 
&input=Museum%20of%20Contemporary%20Art%20Australia                              #I believe %20 is a space 
&inputtype=textquery                                                             #Sets text
&key=AIzaSyBe33L7Etyg7QZFdEfqOyHgvuqLh2Ul0yE                                     #applies the KEY


FIELDS: Asking what you would like to return 
INPUT: What to search for
INPUTTYPE: What is it expecting
KEY: API key 
'''

data = {
    "fields":"formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry%2Cphotos",
    "input":"mongolian",
    "inputtype":"textquery",
    "locationbias":r"circle%3A2000%4047.6918452%2C-122.2226413"
}   
# thepage = urllib.request.urlopen(TESTURL) # Produces a request object
# soup = BeautifulSoup(thepage, "html.parser") # Takes Request and puts it into bs4 Object
# site_json = json.loads(soup.text) # Turns Bs4 Obj into txt into Dict
# print(site_json["candidates"][0]["formatted_address"])
# print(soup.prettify())
# print(soup.prettify())
class G_Places():   
    def __init__(self,input:str, location) -> None:
        self.URL = PLACESURL
        self._orem_coord = 1
        self._af_coord = 1
        self.query_stirng = {
                            "fields":"formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry%2Cphotos",
                            "input":"mongolian",
                            "inputtype":"textquery",
                            "locationbias":r"circle%3A2000%4047.6918452%2C-122.2226413",
                            "key":KEY
                            }
        
    def format_query_string(self):        
        for i in data.keys():
            print(f"&{i}={data[i]}")


