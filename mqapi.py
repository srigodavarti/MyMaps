import json
import urllib.parse
import urllib.request

#Register for an API Key from MapQuest
#API_KEY = ''
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route'
ELEVATION_URL_BASE = 'http://open.mapquestapi.com/elevation/v1/profile'

def get_result(url: str) -> dict:
    ''' issues HTTP request, gets HTTP response, and converts response to a dictionary'''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()

def build_search_url(from_location: str, to_locations: [(str, str)]) -> str:
    ''' takes in parameters and builds a search url'''
    parameters = [('key', API_KEY), ('from', from_location)]
    query_parameters = parameters + to_locations
    
    return BASE_MAPQUEST_URL+'?'+urllib.parse.urlencode(query_parameters)

def build_elevation_url(latlng:str) -> str:
    ''' builds url used to find elevation'''
    parameters = [('key', API_KEY),('shapeFormat', 'raw'),('unit', 'f'),
                  ('latLngCollection',latlng)]

    return ELEVATION_URL_BASE+'?'+urllib.parse.urlencode(parameters)
