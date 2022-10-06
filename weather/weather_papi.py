from weather import weather_sapi
import pprint

def get_periods(coordinates):
    print("Now inside the papi", coordinates)
    response = weather_sapi.get_sapi_response(coordinates)
    print(response)
    periods = response["properties"]["periods"]
    #pprint.pprint(periods)
    return periods[0]


