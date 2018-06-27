##-
###- Web whatsapp based message sending automation
##Author : Jagmeet

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keysa
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
 
# Replace below path with the absolute path
# to chromedriver in your computer
web= webdriver.Chrome('/Users/macuser/Documents/Python/chromedriver')
#Put weblink for whatapp
web.get("https://web.whatsapp.com/")
 
# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
searchName = 'Jagmeet MCQ'
target = '"Jagmeet MCQ"'
 
# Replace the below string with your own message
msgString = "Hi how are you. This automation suite sends message and attachment autmatically via whatsapp"

wait = WebDriverWait(web, 600)
#wait for 20 seconds for intial login
#in this time use your phone to login to web whatsapp by scanning QR code
time.sleep(20)

#Search name of the person to whom you want to send the message 
searchBox=web.find_element_by_xpath('//*[@title="Search or start new chat"]')
searchBox.send_keys(searchName)
#seep for search to give results
time.sleep(1)

#Click on the name found
x_arg = '//span[contains(text(),'+ target + ')]'
group_title = wait.until(EC.visibility_of_element_located((By.XPATH, x_arg)))
group_title.click()

# Send the message though the input box
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
input_box.send_keys(msgString + Keys.ENTER)

# Add attachment 
# Click attach clip button
attachButton_xpath = '//*[@data-icon="clip"]'
searchAttachButton = web.find_element_by_xpath(attachButton_xpath)
searchAttachButton.click()

# Name of file to be attached
fileName = '/Users/macuser/Desktop/Sample.mp4'
# Emulate send keys as if the file was searched 
file_xpath = '//*[@type="file"]'
web.find_element_by_xpath(file_xpath).send_keys(fileName)

# Wait for send button to appear and then Click it
sendButton_xpath = '//*[@data-icon="send-light"]'
wait.until(EC.visibility_of_element_located((By.XPATH, sendButton_xpath))).click()

#To complete a bulky attachment, else this time can be reduced from 15 seconds to 2 seconds
time.sleep(15)

web.quit()
