import weather.weather_sapi
import weather.weather_papi
import callAppleScript

def send_weather(phone_number,coordinates):

    #print("Now inside the weather chain",coordinates)
    message = weather.weather_papi.get_periods(coordinates)
   # print("retrieved message, preparing to send message", message)
    callAppleScript.send_message(phone_number,message)
    return "Successfully sent weather"
