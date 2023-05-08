import pandasreader as pdr
import whatsapp_auto as ws_auto
from FaceRecognizer import FaceRecognizer

file1 = pdr.ExcelReader("/home/mohakborole/Desktop/Projects/Visitors_managenemt_sys/testdata.xlsx", "Sheet1")
visitor = pdr.ExcelReader.read_data(file1)
name_list = visitor[1]
phone_number = visitor[2]
roll_number = visitor[0]

Detector = FaceRecognizer()

available = True
if available:
    message = "\nYou may come in"
else:
    message = "\nPlease visit laters"

while True:
    NameOfVisitor = Detector.faceRecognition()
    if NameOfVisitor in name_list:
        visitorNumber = name_list.index(NameOfVisitor)
        sendto = ws_auto.WhatsAppMessageSender('+91'+ str(phone_number[visitorNumber]), "Hello "+ NameOfVisitor + message)
        ws_auto.WhatsAppMessageSender.send_message(sendto)