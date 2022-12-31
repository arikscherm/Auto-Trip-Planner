import requests 
import urllib3
urllib3.disable_warnings()
import json

#Get list of all locations in index
def get():
    url = 'https://localhost:9200/location/_search'
    headers = {
    'Authorization': 'Basic ZWxhc3RpYzowOERxcVpRU1NJRDBZbUYtYkp4SQ==',
    'Accept':'application/json'
    }
    response = requests.get(url, headers=headers, verify=False) 
    hits = response.json()["hits"]["hits"]
    stored_locations = [i['_id'] for i in hits]
    return stored_locations



def is_location_cached(location):
    cached_locations = get()
    if(location in cached_locations):
        return True
    return False
