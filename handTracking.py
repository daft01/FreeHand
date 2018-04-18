import cv2
import numpy as np

cap = cv2.VideoCapture(1)
#creating camera object
while( cap.isOpened() ):
    ret, vid = cap.read() #reading the frames
    cv2.imshow('regular', vid) #displaying the frames
    gray = cv2.cvtColor(vid,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh1 = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow('contour', thresh1)
    k = cv2.waitKey(10)
    if k == 27:
       break
