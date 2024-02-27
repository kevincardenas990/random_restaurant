""""""
import googlemaps
from datetime import datetime
from constants import KEY 

from constants import KEY

class Gdirections():
    def __init__(self, start=None, end=None) -> None:    
        self.gmaps = googlemaps.Client(KEY)
        self.start = start
        self.end = end
        self.start_time = datetime.now()
        self._raw_data = self.get_raw_data()

    def get_current_location(self):
        '''Unsure how you'd be able to'''
        pass

    def get_raw_data(self, mode="driving"):
        print(self.start, self.end)
        if self.start is None or self.end is None:
            return None
        
        data = self.gmaps.directions(self.start, self.end, mode=mode, departure_time=self.start_time)
        if data:
            return data[0]["legs"][0]
        else:
            print(f"ERROR: {data}")
    
    def get_arrival_time(self):
        '''Returns str of time'''
        return self._raw_data["duration_in_traffic"]['text']
    
    def update_info(self, start, end ):
        self.start, self.end =start, end
        self._raw_data=self.get_raw_data()

    def write_txt(self, items):
        with open("Google_Json.txt", 'w') as in_file:
                in_file.write(str(items))

if __name__ == "__main__":
    direction = Gdirections("818 E 500 S American Fork", "1001 Campus Dr Orem")
    direction.write_txt(direction.get_raw_data())
    print(direction.get_arrival_time())