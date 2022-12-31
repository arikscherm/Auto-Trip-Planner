import requests 
import urllib3
urllib3.disable_warnings()
import json

def publish(message_text,payload):
    url = f'https://localhost:9200/location/_doc/{message_text}'
    headers = {
    'Authorization': 'Basic ZWxhc3RpYzowOERxcVpRU1NJRDBZbUYtYkp4SQ=='
    }
    response = requests.post(url, headers=headers, verify=False, json=payload) 
    return response