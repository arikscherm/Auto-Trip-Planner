from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#This is a placeholder url. It will eventually be set by a geocoded message
url = 'https://www.summitpost.org/longs-peak/150310'


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()),options=options)
driver.get(url)
time.sleep(1)
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
driver.find_element(by=By.XPATH, value = '//*[@id="globalWrapper"]/div[3]/div[3]/div/div[2]/div/div[2]').screenshot('beta/beta.png')

driver.close()
driver.quit()

#TODO: do 14ers.com and all trails, ryan in the SW