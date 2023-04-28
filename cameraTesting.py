import numpy as np
import cv2
cap = cv2.VideoCapture(0)

cap.set(3,640) # set Width
cap.set(4,480) # set Height

while(True):
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #img = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB);

    cv2.imshow('Visitor management System', frame)
    #cv2.imshow('gray', gray)
    
    k = cv2.waitKey(1)
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
