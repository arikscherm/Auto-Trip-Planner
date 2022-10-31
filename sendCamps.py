import campsites.freecampsitesnet
import campsites.find_close_camps
import callAppleScript
import time

    

def send_campsites(phone_number,coordinates):
    
    exec = campsites.freecampsitesnet.write_text_file(coordinates)
    campsites_message = campsites.find_close_camps.prepare_message(coordinates)
    print("sending message")
    #print(len(campsites_message))
    #print(campsites_message)
    callAppleScript.divide_and_send_message(phone_number,campsites_message)
    time.sleep(1)
    return "Successfully sent campsites"


#send_campsites("14145736394",{"latitude":37.2753,"longitude":-107.8801})