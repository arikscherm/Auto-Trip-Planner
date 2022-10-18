import requests
import json
import pprint


#Uses coordinates to obtain three endpoints to call
#get_sapi_response may be used to obtain the forecast, hourly forecast and the forecast zone. 
def get_coordinates_json_response(coordinates):
    coordinates_url = "https://api.weather.gov/points/{},{}".format(coordinates["latitude"],coordinates["longitude"])
    #print("MAKING COORDINATES REQUEST TO ", coordinates_url)
    coordinates_url_response = requests.get(coordinates_url)
    coordinates_json_response = json.loads(coordinates_url_response.text)
       
    #pprint.pprint(coordinates_json_response["properties"])
    return coordinates_json_response


def check_if_404(coordinates_json_response):
    if("status" in coordinates_json_response and coordinates_json_response["status"] == 404): 
        return True
    else:
        return False



#This endpoint includes forecast for days and nights for one week
def get_forecast(coordinates):
    coordinates_json_response = get_coordinates_json_response(coordinates)
    if(check_if_404(coordinates_json_response)): return "Data Unavailable For Requested Point"
    grid_endpoint = coordinates_json_response["properties"]["forecast"]
    forecast_response = requests.get(grid_endpoint)
    return json.loads(forecast_response.text)


#This includes an hourly forecast for one week
def get_forecastHourly(coordinates):
    coordinates_json_response = get_coordinates_json_response(coordinates)
    if(check_if_404(coordinates_json_response)): return "Data Unavailable For Requested Point"
    grid_endpoint = coordinates_json_response["properties"]["forecastHourly"]
    forecastHourly_response = requests.get(grid_endpoint)
    return json.loads(forecastHourly_response.text)
    

#This retrieves where the weather data is coming from
def get_forecastZone(coordinates):
    coordinates_json_response = get_coordinates_json_response(coordinates)
    if(check_if_404(coordinates_json_response)): return "Data Unavailable For Requested Point"
    grid_endpoint = coordinates_json_response["properties"]["forecastZone"]
    forecastZone_response = requests.get(grid_endpoint)
    return json.loads(forecastZone_response.text)





