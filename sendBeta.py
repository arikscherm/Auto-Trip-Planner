import beta.screenshot_beta
import callAppleScript


def send_beta(phone_number):
    #beta = beta.screenshot_beta.screenshot() #most likely will need to replace this line with open png
    beta = "/Users/arischermer/Desktop/code/AutoTripPlanner/beta/beta.png"
    callAppleScript.send_message(phone_number,beta)
    return "Successfully sent beta"

send_beta("<RECIPIENT PHONE NUMBER HERE>")

#Unsure why the image no longer loads