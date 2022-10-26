import beta.screenshot_beta
import callAppleScript
import os
import time


def send_beta(phone_number,message_text):
    status = beta.screenshot_beta.get_beta(message_text)
    if(status == "Unable to find information on summitpost"):
        callAppleScript.send_message(phone_number,status)
        return "Sucessfully sent error message: Beta not found"
    
    cover_image_screenshot = "/<Directory of Project>/beta/cover_image.png"
    beta_screenshot = "/<Directory of Project>/beta/beta.png"

    
    callAppleScript.send_message(phone_number,cover_image_screenshot)
    time.sleep(1)
    callAppleScript.send_message(phone_number,beta_screenshot)
    
    return "Successfully sent beta"
