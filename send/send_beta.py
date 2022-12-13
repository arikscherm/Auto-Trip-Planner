import send.beta.summitpost.screenshot_beta
import send.call_apple_script
import time
import os


def send_beta(phone_number,message_text):
    status = send.beta.summitpost.screenshot_beta.get_beta(message_text)
    if(status == "Unable to find information on summitpost"):
        send.call_apple_script.send_message(phone_number,status)
        return "Sucessfully sent error message: Beta not found"
    
    cover_image_screenshot = os.environ.get('HEFTYFISH_PROJECT_LOCATION')+"/send/beta/summitpost/cover_image.png"
    beta_screenshot = os.environ.get('HEFTYFISH_PROJECT_LOCATION')+ "/send/beta/summitpost/beta.png"

    
    send.call_apple_script.send_message(phone_number,cover_image_screenshot)
    time.sleep(1)
    send.call_apple_script.send_message(phone_number,beta_screenshot)
    
    return "Successfully sent beta"
