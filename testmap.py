# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 23:59:05 2019

@author: Joshua
"""

import json
import urllib.request
import re

map_api_key = 'AIzaSyDIQ1V8MHyE9LrhmCK4rj0q1lagVsSk09k'

dest_a = input('Starting Location:').replace(" ", "+")
dest_b = input('Destination:').replace(" ", "+")

url = 'https://maps.googleapis.com/maps/api/directions/json?origin=' + str(dest_a) + '&destination=' + str(dest_b) + '&key=' + str(map_api_key)

json_obj  = urllib.request.urlopen(url)
data = json.load(json_obj)

def distance():
    return data['routes'][0]['legs'][0]['distance']['text']

def duration():
    return data['routes'][0]['legs'][0]['duration']['text']

def steps():
    for x in data['routes'][0]['legs'][0]['steps']:
        print(clean(x['html_instructions'].replace('<', ' (').replace('>', ') ')))
    return 'End'
        
def clean(string):
    return re.sub(r" ?\([^)]+\)", "", string)

 
print(distance())
print(duration())
print(steps())