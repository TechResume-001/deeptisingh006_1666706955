##-
###- Web whatsapp based message sending automation
##Author : Jagmeet

import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException,
)
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 




#from selenium.common.exceptions import NoSuchElementException

 
# Replace below path with the absolute path
# to chromedriver in your computer
web=webdriver.Chrome('./chromedriver')
#Put weblink for whatapp
web.get("https://web.whatsapp.com/")
wait = WebDriverWait(web, 600)
#wait for 20 seconds for intial login
#in this time use your phone to login to web whatsapp by scanning QR code
time.sleep(20)
# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
FriendsList = [
'Rahul Chowdhary MCQ',
'Jitender Narula NWM',
'Jatinder Raheja',
'Vikas Macquarie MCQ',
'Pooja Anurag MalindaGates',
'Heena bhabhi New'
]
#target = '"Deepti Singh"'

for searchName in FriendsList: 
    
    img = Image.open('HNY2022.jpg')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/Library/Fonts/Comic.ttf', 144)
    
    # Replace the below string with your own message
    
    msgString = " Hi "+ searchName.split()[0] + ",\n Wishing You and Your family \n A Healthy, Wealthy, Safe and a Prosperous\n New  Year - 2022 \n\n\n\n  Regards \n Jagmeet & Deepti"
    draw.text((2650, 500),msgString,fill="white",font=font)
    filenameSave='/Users/macuser/dev/WappWishes/HNY2022.out.'+searchName.split()[0]+'.jpg'
    img.save(filenameSave)
    #Search name of the person to whom you want to send the message 
    #web.find_element_by_xpath("//option[@value='T_U0']").click() 
    #searchBox=web.find_elements_by_xpath("//*[contains(text(), 'Search or start new chat')]")
    #searchBox=web.find_element_by_xpath('//*[@title="Search or start new chat"]')
    #searchBox=web.find_element_by_class_name('_13NKt copyable-text selectable-text')
    searchBox=wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
    searchBox.clear()
    searchBox.send_keys(searchName)
    searchBox.send_keys(Keys.ENTER)


    #Click on the name found
    x_arg = '//span[contains(text(),"'+ searchName + '")]'
    group_title = wait.until(EC.visibility_of_element_located((By.XPATH, x_arg)))
    group_title.click()

    
    # Send the message though the input box
    inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    #input_box.send_keys(msgString + Keys.ENTER)

    # Add attachment 
    # Click attach clip button
    attachButton_xpath = '//*[@data-icon="clip"]'
    searchAttachButton = web.find_element_by_xpath(attachButton_xpath)
    searchAttachButton.click()

    # Name of file to be attached
    fileName = filenameSave
    # Emulate send keys as if the file was searched 
    file_xpath = '//*[@type="file"]'
    web.find_element_by_xpath(file_xpath).send_keys(fileName)

    # Wait for send button to appear and then Click it
    sendButton_xpath = '//*[@data-icon="send"]'
    wait.until(EC.visibility_of_element_located((By.XPATH, sendButton_xpath))).click()

    #To complete a bulky attachment, else this time can be reduced from 15 seconds to 2 seconds
    time.sleep(6)

#web.quit()