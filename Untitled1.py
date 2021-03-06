
# coding: utf-8

# # Gesture Control Project
# 

# ## Semester 1 (2018-2019)
# ## Python Code
# 

# In[ ]:


import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('com4',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    print("Started")
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print (incoming)
    
    if 'Play/Pause' in incoming:
        pyautogui.typewrite(['space'], 0.2)
        print("Play/Pause")

    if 'Rewind' in incoming:
        pyautogui.hotkey('ctrl', 'left')  
        print("Rewind")

    if 'Forward' in incoming:
        pyautogui.hotkey('ctrl', 'right') 
        print("Forward")

    if 'Vup' in incoming:
        pyautogui.hotkey('ctrl', 'down')
        print("Vup")

    if 'Vdown' in incoming:
        pyautogui.hotkey('ctrl', 'up')
        print("Vdown")

    incoming = "";
    
 

