import cv2
import numpy as np

colors = [(0,0,255), (0,128,255), (0,255,255), (0,255,0), (255,255,0), (255,0,0), (255,0,127), (255,51,255), (255,255,255)]
colorIndex = 0
windowHeight = 900
windowWidth = 1500
sizeOfColorChoices = 100
sizeOfmenuWindow = 170
sizeOfCalculator = 700
sizeOfCalButtons = 150
choice = "Calculator"

img = np.zeros((windowHeight,windowWidth,3), np.uint8)

def setMenu():
	cv2.rectangle(img,(windowWidth-sizeOfmenuWindow,0),(windowWidth, 100),(255,255,255),-1)
	cv2.putText(img, "Paint", (windowWidth-sizeOfmenuWindow+30,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)

	cv2.rectangle(img,(windowWidth-sizeOfmenuWindow,110),(windowWidth, 210),(255,255,255),-1)
	cv2.putText(img, "Piano", (windowWidth-sizeOfmenuWindow+30,170), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)

	cv2.rectangle(img,(windowWidth-sizeOfmenuWindow,220),(windowWidth, 320),(255,255,255),-1)
	cv2.putText(img, "Calculator", (windowWidth-sizeOfmenuWindow,280), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)

def setColors():
    for i in range(9):
        cv2.rectangle(img,(0,sizeOfColorChoices*i),(sizeOfC olorChoices, sizeOfColorChoices*i+sizeOfColorChoices), colors[i] ,-1)

def setCalculator():
    cv2.rectangle(img,(int(windowWidth/2-sizeOfCalculator/2), 0),(int(windowWidth/2+sizeOfCalculator/2), windowHeight),(0,255,0),2)
    cv2.rectangle(img,(int(windowWidth/2-sizeOfCalculator/2)+10, 10),(int(windowWidth/2+sizeOfCalculator/2)-10, sizeOfCalButtons),(0,255,0),2)

    cv2.rectangle(img,(((int(windowWidth/2-sizeOfCalculator/2)+10+), int(windowWidth/2-sizeOfCalculator/2) ), (),(0,255,0),2)
			

def move(event,x,y,flags,param):
   
    global colorIndex
    global img
    global choice

    if x > windowWidth - sizeOfmenuWindow and y < 320:
        if y < 100:
            choice = "paint"
            img = np.zeros((windowHeight,windowWidth,3), np.uint8)
            setColors()
        elif y < 210:
            choice = "piano"
            img = np.zeros((windowHeight,windowWidth,3), np.uint8)
        elif y < 320:
            choice = "calculator"
            img = np.zeros((windowHeight,windowWidth,3), np.uint8)
            setCalculator()

        setMenu()
    
    if choice is "paint":
        if x < sizeOfColorChoices:
        
            for i in range(9):
                if y < sizeOfColorChoices * i + sizeOfColorChoices:
                    colorIndex = i
                    break

        if event == cv2.EVENT_MOUSEMOVE:
            cv2.circle(img,(x,y),12, colors[colorIndex], -1)


cv2.namedWindow('image')
cv2.setMouseCallback('image',move)
setMenu()
setColors()

while(1):
    
    cv2.imshow('image',img)
    
    if cv2.waitKey(20) & 0xFF == 113:
        break

cv2.destroyAllWindows()
