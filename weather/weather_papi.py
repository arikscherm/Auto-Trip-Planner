from weather import weather_sapi
import pprint

def get_periods():
    response = weather_sapi.get_sapi_response()
    periods = response["properties"]["periods"]
    #pprint.pprint(periods)
    return periods[0]


#TODO: reduce what the weather papi returns