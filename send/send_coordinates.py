import send.geocode.geocode
import send.call_apple_script

def getCoordinates(message_text):
    coordinates = str(send.geocode.geocode.get_coordinates(message_text))
    if(coordinates == "None"): 
        coordinates = "Unable to find location. Please try again."
        return coordinates
    else:
        coordinates = coordinates.replace('(','')
        coordinates = coordinates.replace(')','')
        coordinates = coordinates.replace(' ','')
        return coordinates

def get_dict_coordinates(message_text):
    coordinates = getCoordinates(message_text)
    coordinates = coordinates.split(',')
    dict_coordinates = {"latitude" : coordinates[0], "longitude" : coordinates[1]}
    return dict_coordinates


def send_coordinates(phone_number,coordinates):
    send.call_apple_script.send_message(phone_number,coordinates)