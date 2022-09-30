import campsites.freecampsitesnet
import callAppleScript

def send_campsites(phone_number):
    f = open("campsites/results.txt")
    campsites_message = f.read()
    print(campsites_message[0:20])
    callAppleScript.send_message(phone_number,campsites_message[0:20])
    return "Successfully sent campsites"


send_campsites("<RECIPIENT PHONE NUMBER HERE>")