import send.beta.summitpost.screenshot_beta
import send.callAppleScript
import os
import time


def send_beta(phone_number,message_text):
    status = send.beta.summitpost.screenshot_beta.get_beta(message_text)
    if(status == "Unable to find information on summitpost"):
        send.applescript.callAppleScript.send_message(phone_number,status)
        return "Sucessfully sent error message: Beta not found"
    
    cover_image_screenshot = "/Users/<Directory of Project>/heftyFish/send/beta/summitpost/cover_image.png"
    beta_screenshot = "/Users/<Directory of Project>/heftyFish/send/beta/summitpost/beta.png"

    
    send.callAppleScript.send_message(phone_number,cover_image_screenshot)
    time.sleep(1)
    send.callAppleScript.send_message(phone_number,beta_screenshot)
    
    return "Successfully sent beta"
