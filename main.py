import geocode.geocode as geocode
import connectChatDB
import time
from datetime import datetime
import sendWeather
import sendCoordinates
import sendBeta
import sendCamps



def check_for_new_message(time_of_last_message):
    new_message = False
    while(new_message == False):
        new_message_data = connectChatDB.execute_query()
        new_message_date = datetime.strptime(new_message_data[3],'%Y-%m-%d %H:%M:%S')
        if(new_message_date > time_of_last_message):
            new_message = True
            return new_message_data
        else:
            print("Nothing new")
            time.sleep(10)
    

def run():
    time_of_last_message = datetime.now()
    message_text = ""
    while(message_text != "end"):
        new_message_data = check_for_new_message(time_of_last_message)
        phone_number = str(new_message_data[1])
        message_text = new_message_data[2].replace('.','')
        time_of_last_message = datetime.strptime(new_message_data[3],'%Y-%m-%d %H:%M:%S')

        

        coordinates = sendCoordinates.getCoordinates(message_text)
        dict_coordinates = sendCoordinates.get_dict_coordinates(message_text)

        
        sendCoordinates.sendCoordinates(phone_number,coordinates)
        sendWeather.send_weather(phone_number,dict_coordinates)
        sendBeta.send_beta(phone_number,message_text)
        sendCamps.send_campsites(phone_number,dict_coordinates)
        


run()