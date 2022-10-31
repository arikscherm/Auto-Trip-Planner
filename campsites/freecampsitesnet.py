from asyncore import write
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

#This is a clean script. No handling for click exception yet.

def open_driver(coordinates,headless):
    options = webdriver.ChromeOptions()
    options.headless = headless
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()),options=options)
    #driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    print("Retrieving freecampsitesnet URL")
    driver.get("https://freecampsites.net/#!({},%20+{})".format(coordinates["latitude"],coordinates["longitude"]))
    driver.implicitly_wait(1)
    return driver


#Get list of all images on map
#Find which of those images are a green tent (denoting a free campsite)
def find_free_camps(driver):
    print("Finding list of potential campsites")
    #Get list of all images on map
    camps = driver.find_elements(by=By.XPATH, value = "//div[@class = 'leaflet-pane leaflet-marker-pane']/img")
    print("Found {} potential in range campsites".format(len(camps)))
    free_camps = []
    for camp in camps:
        #Filter green tents
        if(camp.get_attribute('src') == 'https://freecampsites.net/wp-content/themes/freecampsites/images/map-icons/fc_icon-tent-green-24x24.png'):
            free_camps.append(camp)
    print("Found {} free campsites".format(len(free_camps)))
    return free_camps


def click_tent_icon(camp):
    #Click on green tent to make the popup link appear
    try:
        camp.click()
        time.sleep(4)
    except:
        print("Click exception came up. This should cause the previous campsite to be repeated in the txt file.")

def  get_campsite_html(driver):
    #Grab url from the popup link.
    excerpt = driver.find_elements(by=By.XPATH, value = "//*[@id='map_canvas']/div[1]/div/a")
    src = excerpt[0].get_attribute("href")
    #Extract the parameters from the url. For some reason javascript assumes you are traveling within the domain so no need to include "www.freecampsites.net"
    params = src.split(".net/",1)[1]
    #Use javascript to open up link in new tab
    javascript = "window.open('{}', '_blank').focus()".format(params)
    driver.execute_script(javascript)
    #Switch to new tab
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(7)
    #Extract html
    html = driver.page_source
    return html



#Grab useful text from the info page html.
def get_campsite_text(html):
    soup = BeautifulSoup(html,'lxml')
    #replace <br> tags with '\n' for the purpose of formatting the message
    for br in soup.find_all("br"):
        br.replace_with("\n")
    

    try:
        camp_info = (
         soup.find_all(class_='postTitle')[0].text + '\n' +  #Name of campsite
        soup.select("#overview_box_top_left")[0].text +#Address
        soup.select("#overview_box_top_right")[0].text +#Management
        soup.select("#overview_box_text_bottom")[0].text.replace('\n' '\n','\n') + #Notes
        soup.select("#notes")[0].text.replace('\n' '\n','\n') + '*' + '\n'
       # soup.select('#comment_wrapper') + '\n'
        )
        
        # print("postTitle",soup.find_all(class_='postTitle')[0].text + '\n')  #Name of campsite
        # print("top-left",soup.select("#overview_box_top_left")[0].text)#Address
        # print("top-right",soup.select("#overview_box_top_right")[0].text)#Management
        # print("text_bottom",soup.select("#overview_box_text_bottom")[0].text) #Notes
        # print("notes",soup.select("#notes")[0].text)
    except Exception as e:
        print(e)
        print("something went wrong in campsite text")
        
    return camp_info

def create_message(free_camps,driver):
    success = 0
    fails = 0
    message = ""

    for i in range(len(free_camps)):
        try:
            click_tent_icon(free_camps[i])
            html = get_campsite_html(driver)
            message += get_campsite_text(html)
            success += 1
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            print("Successfully added campsite no {}".format(i))
        except Exception as e: 
            print("unable to add campsite no {}".format(i))
            fails += 1
            print(e)
    print("success {}".format(success))
    print("fail {}".format(fails))
    return message

def write_text_file(coordinates):
    driver = open_driver(coordinates,headless=True)
    free_camps = find_free_camps(driver)
    message = create_message(free_camps,driver)
    f = open("campsites/results.txt",'w')
    f.write(message)
    f.close()
    driver.quit()
