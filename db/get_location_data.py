import requests 
import urllib3
urllib3.disable_warnings()
import json

def get(location):
    url = f'https://localhost:9200/location/_search?q=_id:{location}'
    headers = {
    'Authorization': 'Basic ZWxhc3RpYzowOERxcVpRU1NJRDBZbUYtYkp4SQ==',
    'Accept':'application/json'
    }
    response = requests.get(url, headers=headers, verify=False) 
    try:
        hits = response.json()["hits"]["hits"][0]
        location_data = {"location":hits['_id'],"gps":hits['_source']['gps'],"camping":hits['_source']['camping'],"beta":hits['_source']['beta']}
    except:
        print("Incomplete information found in database. Will now try retrieving information and updating the database.")
        return False
    return location_data