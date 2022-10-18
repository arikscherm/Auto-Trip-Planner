import weather.weather_sapi
import weather.weather_papi
import callAppleScript
import time

def send_weather(phone_number,coordinates):

    #print("Now inside the weather chain",coordinates)
    message = weather.weather_papi.get_weather(coordinates)
   # print("retrieved message, preparing to send message", message)
    callAppleScript.send_message(phone_number,message[0])
    time.sleep(2)
    callAppleScript.send_message(phone_number,message[1])
    time.sleep(2)
    callAppleScript.send_message(phone_number,message[2])
    return "Successfully sent weather"
