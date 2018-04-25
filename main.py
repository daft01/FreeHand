import cv2
import numpy as np

color = (255,0,0)
windowHeight = 900
windowWidth = 1500
sizeOfColorChoices = 100
sizeOfmenuWindow = 170 
choice = "paint";
img = np.zeros((windowHeight,windowWidth,3), np.uint8)

def setMenu():
	cv2.rectangle(img,(windowWidth-sizeOfmenuWindow,0),(windowWidth, 100),(255,255,255),-1)
	cv2.putText(img, "Paint", (windowWidth-sizeOfmenuWindow+30,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)

	cv2.rectangle(img,(windowWidth-sizeOfmenuWindow,110),(windowWidth, 210),(255,255,255),-1)
	cv2.putText(img, "Piano", (windowWidth-sizeOfmenuWindow+30,170), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)

	cv2.rectangle(img,(windowWidth-sizeOfmenuWindow,220),(windowWidth, 320),(255,255,255),-1)
	cv2.putText(img, "Calculator", (windowWidth-sizeOfmenuWindow,280), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)

def setColors():
    cv2.rectangle(img,(0,0),(sizeOfColorChoices, sizeOfColorChoices),(0,0,255),-1)

    cv2.rectangle(img,(0,sizeOfColorChoices),(sizeOfColorChoices, sizeOfColorChoices*2),(0,128,255),-1)

    cv2.rectangle(img,(0,sizeOfColorChoices*2),(sizeOfColorChoices, sizeOfColorChoices*3),(0,255,255),-1)

    cv2.rectangle(img,(0,sizeOfColorChoices*3),(sizeOfColorChoices, sizeOfColorChoices*4),(0,255,0),-1)

    cv2.rectangle(img,(0,sizeOfColorChoices*4),(sizeOfColorChoices, sizeOfColorChoices*5),(255,255,0),-1)

    cv2.rectangle(img,(0,sizeOfColorChoices*5),(sizeOfColorChoices, sizeOfColorChoices*6),(255,0,0),-1)

    cv2.rectangle(img,(0,sizeOfColorChoices*6),(sizeOfColorChoices, sizeOfColorChoices*7),(255,0,127),-1)

    cv2.rectangle(img,(0,sizeOfColorChoices*7),(sizeOfColorChoices, sizeOfColorChoices*8),(255,51,255),-1)

    cv2.rectangle(img,(0,sizeOfColorChoices*8),(sizeOfColorChoices, sizeOfColorChoices*9),(255,255,255),-1)

def move(event,x,y,flags,param):
   
	if choice is "paint":
		
		global color

		if x < sizeOfColorChoices:
			if y < sizeOfColorChoices:
				color = (0,0,255)
			elif y < sizeOfColorChoices*2:
				color = (0,128,255)
			elif y < sizeOfColorChoices*3:
				color = (0,255,255)
			elif y < sizeOfColorChoices*4:
				color = (0,255,0)
			elif y < sizeOfColorChoices*5:
				color = (255,255,0)
			elif y < sizeOfColorChoices*6:
				color = (255,0,0)
			elif y < sizeOfColorChoices*7:
				color = (255,0,127)
			elif y < sizeOfColorChoices*8:
				color = (255,51,255)
			elif y < sizeOfColorChoices*9:
				color = (255,255,255)

		if event == cv2.EVENT_MOUSEMOVE:
			cv2.circle(img,(x,y),8, color, -1)

cv2.namedWindow('image')
cv2.setMouseCallback('image',move)
setMenu()
setColors()

while(1):
    
    cv2.imshow('image',img)
    
    if cv2.waitKey(20) & 0xFF == 113:
        break

cv2.destroyAllWindows()
