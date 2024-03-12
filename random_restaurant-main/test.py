import requests 
from constants import *

TESTURL = "https://places.googleapis.com/v1/places:searchText"

payload ={"key":KEY,  }
def tester():
    response = requests.get(TESTURL, params=payload)
    response_json = response.json()
    print(response_json)

tester()