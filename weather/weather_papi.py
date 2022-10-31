from weather import weather_sapi
#import weather_sapi
from datetime import datetime
import pprint



def process_forecastZone(coordinates):
    forecastZone_response = weather_sapi.get_forecastZone(coordinates)
    if(str(type(forecastZone_response)) == "<class 'str'>"): return forecastZone_response
    forecastName = forecastZone_response["properties"]["name"]
    forecastState = forecastZone_response["properties"]["state"]
    return "View weather for {}, {} below".format(forecastName,forecastState)
   

def process_forecastHourly(coordinates):
    forecastHourly_response = weather_sapi.get_forecastHourly(coordinates)
    if("status" in forecastHourly_response and forecastHourly_response["status"] == 500): 
        return forecastHourly_response["detail"]
    try:
        forecastHourly = forecastHourly_response["properties"]["periods"]
        forecast_message = ""
        start_date = forecastHourly[0]["startTime"][8:10]
        for period in forecastHourly[0:24]:
            full_date = period["startTime"][0:16].replace("T", " ")
            if(int(full_date[12])%2 == 0):
                name = ""

                day = full_date[8:10]
                if(day == start_date):
                    name += "Today, "
                else:
                    name += "Tomorrow, "

                hour = full_date[11:13]
                if(int(hour) > 11):
                    hour = str(int(hour)%12)
                    if(hour == "0"): hour = "12"
                    name += hour + "pm"
                else:
                    if(hour == "00"): hour = "12"
                    hour = hour.lstrip('0')
                    name += hour + "am"


             #   forecast_interval = period["startTime"][0:10]
              #  forecast_name = period["name"]
                temperature = period["temperature"]
                temperature_unit = period["temperatureUnit"]
                wind_speed = period["windSpeed"]
                wind_direction = period["windDirection"]
                if(period["detailedForecast"]):
                    details = period["detailedForecast"]
                else:
                    details = period["shortForecast"]
                forecast_message += name + '\n' + details + '\n' + str(temperature) + ' ' + temperature_unit + '\n' + str(wind_speed) + ' ' + wind_direction + '\n' + '\n'
        return forecast_message
    except:
        return "Weather Data Not Found For Requested Point"
        
    

            


def process_forecast(coordinates):
    forecast_response = weather_sapi.get_forecast(coordinates)
    try:
        forecast = forecast_response["properties"]["periods"]
        forecast_message = ""
        for period in forecast[2:]:
            forecast_interval = period["startTime"][0:10]
            forecast_name = period["name"]
            temperature = period["temperature"]
            temperature_unit = period["temperatureUnit"]
            wind_speed = period["windSpeed"]
            wind_direction = period["windDirection"]
            if(period["detailedForecast"]):
                details = period["detailedForecast"]
            else:
                details = period["shortForecast"]
            forecast_message += forecast_name + ' ' + forecast_interval + '\n' + details + '\n' + str(temperature) + ' ' + temperature_unit + '\n' + str(wind_speed) + ' ' + wind_direction + '\n' + '\n'
        return forecast_message
    except:
        return "Weather Data Not Found For Requested Point"



# 42.515970, -83.150692
# coordinates = {"latitude":42.515970,"longitude":-83.150692}
# print(process_forecastZone(coordinates))
# print(process_forecastHourly(coordinates))
# print(process_forecast(coordinates))

def get_weather(coordinates):
    forecastZone = process_forecastZone(coordinates)
    forecastHourly = process_forecastHourly(coordinates)
    forecast = process_forecast(coordinates)
    return [forecastZone,forecastHourly,forecast]
    





