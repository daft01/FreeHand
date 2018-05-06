import cv2
import numpy as np

palm_cascade = cv2.CascadeClassifier('palm.xml')

if palm_cascade.empty():
    print('WARNING: Fist cascade did not load')

cap = cv2.VideoCapture(0)

while(1):
    ret, videoImg = cap.read()

    gray = cv2.cvtColor(videoImg, cv2.COLOR_BGR2GRAY)
    palm = palm_cascade.detectMultiScale(gray, 1.3,5)


    for(x,y,w,h) in palm:
        cv2.rectangle(videoImg,(x,y), (x+w, y+h), (255,0,0), 2, 2)

    cv2.imshow('img', videoImg)

    if cv2.waitKey(20) & 0xFF == 113:
        break

cv2.destroyAllWindows()
