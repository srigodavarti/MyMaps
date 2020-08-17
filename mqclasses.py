import mqapi

class Directions:
    '''objects which can print out steps'''
    def __init__(self, info: dict):
        self._info = info

    def print_output(self) -> None:
        '''prints out directions'''
        steps = self._info['route']['legs']
        print()
        print("DIRECTIONS")
        for item in steps:
            for element in item['maneuvers']:
                print(element['narrative'])

class Distance:
    '''objects which can print out distance'''
    def __init__(self, info: dict):
        self._info = info

    def print_output(self) -> None:
        '''prints out total distance'''
        distance = int(round(self._info['route']['distance']))          
        print()
        print("TOTAL DISTANCE: ", end = "")
        print(str(distance) + " miles")

class Time:
    '''objects which can print out time'''
    def __init__(self, info: dict):
        self._info = info

    def print_output(self) -> None:
        '''prints out total time'''
        seconds = self._info['route']['time']
        print()
        print("TOTAL TIME: ", end = "")
        time = int(round(seconds/60))
        print(str(time) + " minutes")

class Latlng:
    '''objects which can print out latitudes and longitudes'''
    def __init__(self, info: dict):
        self._info = info

    def print_output(self) -> None:
        '''prints out latitudes and longitudes of each location'''
        latlng_list = _latlng_tuples(self._info)
        print()
        print("LATLONGS")
        for item in latlng_list:
            if item[0] >= 0:
                if item[1]>0:
                    print('%.2f' % item[0] +"N "+ '%.2f' % item[1] +"E")
                else:
                    print('%.2f' % item[0] +"N "+ '%.2f' % abs(item[1]) +"W ")
            else:
                if item[1]>0:
                    print('%.2f' % abs(item[0]) +"S "+ '%.2f' % item[1] +"E")
                else:
                    print('%.2f' % abs(item[0]) +"S "+ '%.2f' % abs(item[1]) +"W ")
   
class Elevation:
    '''objects which can print out latitudes and longitudes'''
    def __init__(self, info: dict):
        self._info = info

    def print_output(self) -> None:
        ''' prints out elevation of each location'''
        latlng_list = _latlng_tuples(self._info)
        print()
        print("ELEVATIONS")
        for item in latlng_list:
            str_item = str(item[0])+ "," + str(item[1])
            elevation_url = mapquestapi.build_elevation_url(str_item)
            elevation_dictionary = mapquestapi.get_result(elevation_url)
            
            for item in elevation_dictionary['elevationProfile']:
                print(round(item['height']))


def _latlng_tuples(info: dict) -> [(float, float)]:
    '''builds a list of tuples with (latitude, longitude)'''
    latlng_list = []
    for item in info['route']['locations']:
        longitude = item['latLng']['lng']     
        latitude = item['latLng']['lat']
        latlng_tuple = (latitude, longitude)
        latlng_list.append(latlng_tuple)
    return latlng_list



