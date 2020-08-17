import mapquestapi
from mapquestclasses import Directions, Distance, Time, Latlng, Elevation
import socket
import urllib

def run_program() -> None:
    '''calls functions to take in user input and produce output'''
    try:
        url = locations()
        actions_list = outputs()
        info = mapquestapi.get_result(url)
        take_action(actions_list, info)
    except KeyError:
        print()
        print('NO ROUTE FOUND')
    except (socket.gaierror, urllib.error.URLError):
        print()
        print('MAPQUEST ERROR')
    else:
        print()
        print('Directions Courtesy of MapQuest; ', end="")
        print('Map Data Copyright OpenStreetMap Contributors')

def locations() -> str:
    ''' takes in locations and returns a url'''
    num_locations = int(input())
    from_location = str(input())
    to_locations = []
    for i in range (0, num_locations-1):
        to_locations.append(str(input()))

    to_locations = locations_tuples(to_locations)

    url = mapquestapi.build_search_url(from_location, to_locations)
    return url 

def locations_tuples(to_locations: [str]) -> [(str, str)]:
    ''' converts destination locations to form of parameter used in url'''
    location_list = []
    for location in to_locations:
        location_tuple = ('to', location)
        location_list.append(location_tuple)
    return location_list

def outputs() -> [str]:
    ''' takes in the outputs the user wants and returns them in a list'''
    num_outputs = int(input())
    outputs = []
    for i in range(0, num_outputs):
        outputs.append(input())

    return outputs

def take_action(actions: [str], info: dict) -> None:
    ''' produces each output in the list of outputs wanted'''
    obj_dict = {"STEPS": Directions(info), "TOTALDISTANCE": Distance(info),
                "TOTALTIME": Time(info), "LATLONG": Latlng(info),
                "ELEVATION": Elevation(info)}
    for item in actions:
        obj_dict[item].print_output()

if __name__ == '__main__':
    run_program()
