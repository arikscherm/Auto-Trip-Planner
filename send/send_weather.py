import send.weather.weather_gov.weather_sapi
import send.weather.weather_gov.weather_papi
import send.call_apple_script
import time

def send_weather(phone_number,coordinates):

    #print("Now inside the weather chain",coordinates)
    message = send.weather.weather_gov.weather_papi.get_weather(coordinates)
   # print("retrieved message, preparing to send message", message)
    send.call_apple_script.send_message(phone_number,message[0])
    time.sleep(2)
    send.call_apple_script.send_message(phone_number,message[1])
    time.sleep(2)
    send.call_apple_script.send_message(phone_number,message[2])
    return "Successfully sent weather"
