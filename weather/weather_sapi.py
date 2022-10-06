import requests
import json

def get_coordinates_endpoint_response(coordinates):
    coordinates_url = "https://api.weather.gov/points/{},{}".format(coordinates["latitude"],coordinates["longitude"])
    print("making coordinates request to ", coordinates_url)
    coordinates_url_response = requests.get(coordinates_url)
    coordinates_json_response = json.loads(coordinates_url_response.text)
    print("for debugging coordinates response -->")
    print(coordinates_json_response)
    return coordinates_json_response

def process_coordinates_response(coordinates_json_response):
    print("processing coordinates json response to prepare grid endpoint")
    grid_endpoint = coordinates_json_response["properties"]["forecast"]
    return grid_endpoint

def get_forecast(grid_endpoint):
    print("making forecast request to ", grid_endpoint)
    forecast_response = requests.get(grid_endpoint)
    return forecast_response.text


def get_sapi_response(coordinates):
    print("now inside the get_sapi_response", coordinates)
    coordinates_json_response = get_coordinates_endpoint_response(coordinates)
    grid_endpoint = process_coordinates_response(coordinates_json_response)
    sapi_response = get_forecast(grid_endpoint)
    return json.loads(sapi_response)

#coordinates = {"latitude" : 37.2753, "longitude" : -107.8801}