from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time



def open_driver(url,headless):
    options = webdriver.ChromeOptions()
    options.headless = headless 
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()),options=options)
    driver.get(url)
    return driver

def navigate_to_beta_page(driver,message_text):
    accept_cookies = driver.find_element(by=By.XPATH, value='//*[@id="CybotCookiebotDialogBodyButtonAccept"]')
    accept_cookies.click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value = '//*[@id="autocomplete-dataset"]').send_keys(message_text)
    time.sleep(3)

    #
    first_result = driver.find_element(by=By.XPATH, value = '/html/body/div[2]/div[1]/div[1]/div[1]/div[2]/form/div/div/span/span/div[1]/span/div[1]/div[1]')
    
    print("clicking first result")
    first_result.click()
    return driver


def get_beta_page_link(driver):
    link_to_beta_page = driver.current_url
    print("retrieved url", link_to_beta_page,"restarting driver")
    driver.close()
    driver.quit()
    return link_to_beta_page




def screenshot(driver):
    
    print("creating lambda function")
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    print("setting window size")
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
    print("finding part to screenshot")
    driver.find_element(by=By.CLASS_NAME, value = 'cover-image-wrap').screenshot('beta/cover_image.png')
    driver.find_element(by=By.CLASS_NAME, value = 'full-content').screenshot('beta/beta.png')
    
   
    print("screenshot created, closing driver")
    #driver.close()
    #driver.quit()



def get_beta(message_text):
    url = "https://www.summitpost.org/"
    driver = open_driver(url,headless=True)
    print(message_text)
    navigate_to_beta_page(driver,message_text)

    #comment out this block for pictures and ads
    # link_to_beta_page = get_beta_page_link(driver)
    # driver = open_driver(link_to_beta_page,headless=True)
    
    
    
    screenshot(driver)
    
    
    
    
#main()


#TODO: do 14ers.com and all trails, ryan in the SW

