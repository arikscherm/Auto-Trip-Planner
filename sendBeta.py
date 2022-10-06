import beta.screenshot_beta
import callAppleScript
import os


def send_beta(phone_number,message_text):
    beta.screenshot_beta.get_beta(message_text)
    beta_screenshot = "/Users/arischermer/Desktop/code/AutoTripPlanner/beta/beta.png"
    cover_image_screenshot = "/Users/arischermer/Desktop/code/AutoTripPlanner/beta/beta/cover_image.png"
    callAppleScript.send_message(phone_number,beta_screenshot)
    callAppleScript.send_message(phone_number,cover_image_screenshot)
    return "Successfully sent beta"
