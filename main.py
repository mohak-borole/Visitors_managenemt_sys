import pandasreader as pdr
import whatsapp_auto as ws_auto

file1 = pdr.ExcelReader("/home/mohakborole/Desktop/Projects/Visitors_managenemt_sys/testdata.xlsx", "Sheet1")
visitor = pdr.ExcelReader.read_data(file1)
name = visitor[1]
phone_number = visitor[2]
roll_number = visitor[0]

available = False
if (available):
    message = ' Please come in'
else:
    message = ' sorry for inconvinience \n Maam is not available'


sendto = ws_auto.WhatsAppMessageSender('+91'+ str(phone_number[0]), "Hello "+ name[0] + message )
ws_auto.WhatsAppMessageSender.send_message(sendto)
