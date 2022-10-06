import os

def send_message(phone_number, message):
    
    send_success = os.system('osascript sendMessage.applescript {} "{}"'.format(phone_number, message))
    if(send_success == 0):
        print("message sent")
    else:   
        print("There was an error sending the message ", message)
