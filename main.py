import cv2
import numpy as np

colors = [(0,0,255), (0,128,255), (0,255,255), (0,255,0), (255,255,0), (255,0,0), (255,0,127), (255,51,255), (255,255,255)]
colorIndex = 0
windowHeight = 720
windowWidth = 1280
sizeOfColorChoices = 80
sizeOfmenuWindow = 170
sizeOfCalculator = 500
sizeOfCalButtons = 100
choice = "paint"

palm_cascade = cv2.CascadeClassifier('palm.xml')

if palm_cascade.empty():
    print('WARNING: palm cascade did not load')

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
        cv2.rectangle(img,(0,sizeOfColorChoices*i),(sizeOfColorChoices*2, sizeOfColorChoices*i+sizeOfColorChoices), colors[i] ,-1)

def setCalculator():
    cv2.rectangle(img,(int(windowWidth/2-sizeOfCalculator/2), 0),(int(windowWidth/2+sizeOfCalculator/2), windowHeight-100),(0,255,0),2)
    cv2.rectangle(img,(int(windowWidth/2-sizeOfCalculator/2)+20, 20),(int(windowWidth/2+sizeOfCalculator/2)-20, sizeOfCalButtons),(0,255,0),2)

    n = int(windowWidth/2-sizeOfCalculator/2)

    for y in range(4):
        for x in range(4):
            cv2.rectangle(img, (sizeOfCalButtons*x+20+(20*x)+n, sizeOfCalButtons*y+10+(20*y)+sizeOfCalButtons),(sizeOfCalButtons*x+sizeOfCalButtons+20+(20*x)+n, sizeOfCalButtons*y+sizeOfCalButtons+20+(20*y)+sizeOfCalButtons),(0,255,0),2)

    for i in range(3):
        cv2.putText(img, str(i+1), (n+50+sizeOfCalButtons*i+(20*i), sizeOfCalButtons*2-10), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "+", (n+50+sizeOfCalButtons*3+(20*3), sizeOfCalButtons*2-25), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    for i in range(3):
        cv2.putText(img, str(i+4), (n+50+sizeOfCalButtons*i+(20*i), sizeOfCalButtons*3+10), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "-", (n+50+sizeOfCalButtons*3+(20*3)-5, sizeOfCalButtons*3), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    for i in range(3):
        cv2.putText(img, str(i+7), (n+50+sizeOfCalButtons*i+(20*i), sizeOfCalButtons*4+20), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "*", (n+50+sizeOfCalButtons*3+5+(20*3), sizeOfCalButtons*4+10), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "-/+", (n+30, sizeOfCalButtons*5+30), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(img, "0", (n+70+sizeOfCalButtons*1, sizeOfCalButtons*5+40), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(img, "=", (n+85+sizeOfCalButtons*2, sizeOfCalButtons*5+40), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(img, "/", (n+105+sizeOfCalButtons*3+10, sizeOfCalButtons*5+35), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2,cv2.LINE_AA)

def setPiano():
    pass
def move(x,y):

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
            setPiano()
        elif y < 320:
            choice = "calculator"
            img = np.zeros((windowHeight,windowWidth,3), np.uint8)
            setCalculator()

        setMenu()

    if choice is "paint":
<<<<<<< HEAD
        if x < sizeOfColorChoices*2:
        
=======
        if x < sizeOfColorChoices:

>>>>>>> 7c8643805810aa937574e73d3779b9a577b9c343
            for i in range(9):
                if y < sizeOfColorChoices * i + sizeOfColorChoices:
                    colorIndex = i
                    break


        cv2.circle(img,(x,y),8, colors[colorIndex], -1)


cv2.namedWindow('image')
setMenu()

setColors()

handWindow = "HandDetection"
cap = cv2.VideoCapture(1)
cv2.namedWindow(handWindow)
cv2.resizeWindow('image', windowWidth,windowHeight)

while(1):
    ret, videoImg = cap.read()
    gray = cv2.cvtColor(videoImg, cv2.COLOR_BGR2GRAY)

<<<<<<< HEAD
    fist = fist_cascade.detectMultiScale(gray, 1.3,5)
	
    for(x,y,w,h) in fist:
=======
    palm = palm_cascade.detectMultiScale(gray, 1.3,5)

    for(x,y,w,h) in palm:
>>>>>>> 7c8643805810aa937574e73d3779b9a577b9c343
        move(windowWidth-x,y)
        cv2.circle(videoImg,(x+int(w/2),y+int(h/2)),12, (0,0,255 ), -1)

    cv2.imshow('img', img)
    cv2.imshow('image', videoImg)
    if cv2.waitKey(20) & 0xFF == 113:
        break

cv2.destroyAllWindows()
