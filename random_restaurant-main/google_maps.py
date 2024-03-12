""""""
import googlemaps
from datetime import datetime
from constants import KEY 

from constants import KEY

class G_Directions():
    def __init__(self, start=None, end=None, mode="driving") -> None:    
        self.gmaps = googlemaps.Client(KEY)
        self._mode= mode
        self._start = start
        self._end = end
        self.start_time = datetime.now()
        self._raw_data = self.get_raw_data()


    def get_current_location(self):
        '''Request Info''' 
        pass

    def get_raw_data(self):
        
        if isinstance(self._start, tuple):
            self._start = self.gmaps.reverse_geocode(self._start)[1]["formatted_address"]

        if isinstance(self._end, tuple):
            self._end = self.gmaps.reverse_geocode(self._end)[1]["formatted_address"]

        if self._start is None or self._end is None:
            return None
        
        data = self.gmaps.directions(self._start, self._end, mode=self._mode, departure_time=self.start_time)
        if data:
            return data[0]["legs"][0]
        else:
            print(f"ERROR: {data}")
    
    def get_arrival_time(self):
        '''Returns str of time'''
        return self._raw_data["duration_in_traffic"]['text']
    
    def update_info(self, start, end ):
        self._start, self._end = start, end
        self._raw_data=self.get_raw_data()

    def write_txt(self, items):
        with open("Google_Json.txt", 'w') as in_file:
                in_file.write(str(items))

    @property
    def start(self):
        return self._start
    
    @start.setter
    def start(self, item):
        if not isinstance(item, str):
            raise ValueError ("Please enter a String")
        self._start = item

    @property
    def end(self):
        return self._end
    
    @end.setter
    def end(self, item):
        if not isinstance(item, str):
            raise ValueError ("Please enter a String")
        self._end = item



if __name__ == "__main__":
    direction = G_Directions("1001 Campus Dr Orem Ut", (40.3769, -111.7958)).get_arrival_time()
    print(direction)
