import pywhatkit as pwk
import pyautogui as pg
import time
import pandas as pd

class WhatsAppMessageSender:
    def __init__(self, time_hours, time_minutes, wait_time=2):
        self.time_hours = time_hours
        self.time_minutes = time_minutes
        self.wait_time = wait_time
    
    def send_message(self, phone_number, message):
        pwk.sendwhatmsg(phone_number, message, self.time_hours, self.time_minutes, True, self.wait_time)
        time.sleep(10)
        pg.press("enter")

class ExcelReader:
    def __init__(self, path, sheet_name='Sheet1'):
        self.path = path
        self.sheet_name = sheet_name

    def read_data(self):
        # Read data from Excel file into a pandas dataframe
        df = pd.read_excel(self.path, sheet_name=self.sheet_name)

        # Access data in the dataframe
        phone_numbers = df['phone_number'].tolist()
        messages = df['message'].tolist()

        return phone_numbers, messages

# Create an instance of ExcelReader and read data from an Excel file
excel_reader = ExcelReader('path/to/excel/file.xlsx')
phone_numbers, messages = excel_reader.read_data()

# Create an instance of WhatsAppMessageSender
sender = WhatsAppMessageSender(14, 3)

# Loop through the phone numbers and messages, and send each message
for phone_number, message in zip(phone_numbers, messages):
    sender.send_message(phone_number, message)
