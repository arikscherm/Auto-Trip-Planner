import os

def send_message(phone_number, message):
    print(message)
    send_success = os.system('osascript sendMessage.applescript {} "{}"'.format(phone_number, message))
    if(send_success == 0):
        print("message sent")
    else:   
        print("There was an error sending the message ", message)


def divide_and_send_message(phone_number,message):
    begin = 0 
    end = 0
    inc = 2047 #max number of letters to be sent
    while(begin < len(message)):
        if((end + inc) > len(message)):
            end = len(message)
            send_message(phone_number,message[begin:end])
            begin = end
        else:
            end += inc
            send_message(phone_number,message[begin:end])
            begin = end