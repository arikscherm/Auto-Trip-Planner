import send.camps.freecampsitesnet.freecampsitesnet
import send.camps.freecampsitesnet.find_close_camps
import send.call_apple_script
import time

    

def send_campsites(phone_number,coordinates):
    
    exec = send.camps.freecampsitesnet.freecampsitesnet.write_text_file(coordinates)
    campsites_message = send.camps.freecampsitesnet.find_close_camps.prepare_message(coordinates)
    print("sending message")
    #print(len(campsites_message))
    #print(campsites_message)
    send.call_apple_script.divide_and_send_message(phone_number,campsites_message)
    time.sleep(1)
    return campsites_message


#send_campsites("14145736394",{"latitude":37.2753,"longitude":-107.8801})