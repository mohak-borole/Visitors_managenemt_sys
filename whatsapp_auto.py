import pywhatkit as pwk
import pyautogui as pg
import time

class WhatsAppMessageSender:
    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message
    
    def send_message(self):
        pwk.sendwhatmsg_instantly(self.phone_number, self.message)
        time.sleep(2)
        pg.press("enter")
        time.sleep(2)
        pg.hotkey('ctrl','w')
