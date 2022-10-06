import geocode.geocode
import callAppleScript

def getCoordinates(message_text):
    coordinates = str(geocode.geocode.get_coordinates(message_text))
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


def sendCoordinates(phone_number,coordinates):
    callAppleScript.send_message(phone_number,coordinates)
