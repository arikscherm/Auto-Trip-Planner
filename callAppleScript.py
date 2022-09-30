import os

def send_message(phone_number, message):
    os.system('osascript sendMessage.applescript {} "{}"'.format(phone_number, message))
    print("message sent")