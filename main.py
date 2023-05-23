import pandasreader as pdr
import whatsapp_auto as ws_auto
from FaceRecognizer import FaceRecognizer
from plyer import notification

file1 = pdr.ExcelReader("/home/mohakborole/Desktop/Projects/Visitors_managenemt_sys/testdata.xlsx", "Sheet1")
visitor = pdr.ExcelReader.read_data(file1)
name_list = visitor[1]
phone_number = visitor[2]
roll_number = visitor[0]

Detector = FaceRecognizer()

def set_message(available):
    if available == 1:
        message = "\nYou may come in"
    elif available == 2:
        message = "\nPlease Wait"
    elif available == 3:
        message = "\nPlease Visit Later"
    return message

def recognizeFaces():
    while True:
        NameOfVisitor = Detector.faceRecognition()
        if NameOfVisitor in name_list:
            visitorNumber = name_list.index(NameOfVisitor)
            break
    notification.notify(
         title = "VISITOR MANAGEMENT SYSTEM",
         message = "You Have a visitor\n" + NameOfVisitor + " Wants Permission to visit you" ,
         #timeout = 10
    )
    return NameOfVisitor , visitorNumber

def send_message(message , NameOfVisitor , visitorNumber):
        sendto = ws_auto.WhatsAppMessageSender('+91'+ str(phone_number[visitorNumber]), "Hello "+ NameOfVisitor + message)
        ws_auto.WhatsAppMessageSender.send_message(sendto)
