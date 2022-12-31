import connect_chat_db
import send.call_apple_script
import send.geocode.geocode as geocode
import send.send_coordinates
import send.send_weather
import send.send_beta
import send.send_camps
from datetime import datetime
import time
import db.publish_new_location
import db.get_all_locations
import db.get_location_data



def check_for_new_message(time_of_last_message):
    new_message = False
    while(new_message == False):
        new_message_data = connect_chat_db.execute_query()
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


        location_data = db.get_location_data.get(message_text)
        if(location_data != False):
        # ### Then we have the gps, beta and camping
            location_data = db.get_location_data.get(message_text)
            send.call_apple_script.send_message(phone_number,location_data["gps"])
            dict_coordinates = send.send_coordinates.get_dict_coordinates(message_text)
            send.send_weather.send_weather(phone_number,dict_coordinates)
            #send.call_apple_script.send_message(phone_number,location_data["beta"])
            #send.call_apple_script.send_message(phone_number,location_data["weather"])
        else:
            coordinates = send.send_coordinates.getCoordinates(message_text)
            dict_coordinates = send.send_coordinates.get_dict_coordinates(message_text)
            send.send_coordinates.send_coordinates(phone_number,coordinates)
            send.send_weather.send_weather(phone_number,dict_coordinates)
            path_to_beta = send.send_beta.send_beta(phone_number,message_text)
            campsites_message = send.send_camps.send_campsites(phone_number,dict_coordinates)
            success = db.publish_new_location.publish(message_text,{"gps":str(coordinates),"beta":path_to_beta,"camps":campsites_message})
            print(success)
#if __name__ == "__main__":
run()