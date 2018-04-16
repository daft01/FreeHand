import cv2
import numpy as np

color = (255,0,0)
windowHeight = 700
windowWidth = 1300

def draw_circle(event,x,y,flags,param):
    
    global color
    
    if x > windowWidth-100:
        if y < 108:
            color = (0, 255, 0)
        elif y < 218:
            color = (0, 0, 255)

    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img,(x,y),8, color, -1)

img = np.zeros((windowHeight,windowWidth,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

cv2.rectangle(img,(windowWidth-100,0),(windowWidth,108),(0,255,0),-1)
cv2.rectangle(img,(windowWidth-100,108),(windowWidth,218),(0,0,255),-1)

while(1):
    cv2.imshow('image',img)
    
    if cv2.waitKey(20) & 0xFF == 113:
        break

cv2.destroyAllWindows()
