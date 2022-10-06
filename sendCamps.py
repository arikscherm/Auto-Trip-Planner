import campsites.freecampsitesnet
import callAppleScript

def send_campsites(phone_number,coordinates):
    campsites.freecampsitesnet.write_text_file(coordinates)
    f = open("campsites/results.txt")
    campsites_message = f.read()
    # print(campsites_message[0:20])
    callAppleScript.send_message(phone_number,campsites_message[0:20])
    return "Successfully sent campsites"


