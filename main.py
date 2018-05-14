'''
COURSE: CST 205 Multimedia Design and Programing
TITLE:  FreeHand
AUTHORS:
            Iris Manriquez | Daniel Morales | Edgar Reyes
DATE:   May 13th, 2018
ABSTRACT:

FreeHand is an open source project that uses OPEN SOURCE COMPUTER VISION to assign computer mouse properties to
a user's hand gestures, such as a fist. The user's hand gestures can then do multiple actions within each individual
application in the program, like play notes in a piano, or paint using various paints and brushstrokes. FreeHand is
essential a program that uses hand recognition to replace the usual computer mouse usage.
'''
import cv2 #cv2 and numpy libraries were used by all group members to create this project.
import numpy as np
import pygame #pygame was individually used by Iris Manriquez to create the piano notes.

colors = [(0,0,255), (0,128,255), (0,255,255), (0,255,0), (255,255,0), (255,0,0), (255,0,127), (255,51,255), (255,255,255)]
toneArray= ["notes/Anote.wav","notes/Bnote.wav","notes/Cnote.wav","notes/Dnote.wav","notes/Enote.wav","notes/Fnote.wav","notes/Gnote.wav"]
blackTones=["notes/AFnote.wav","notes/CSnote.wav","notes/DSnote.wav","notes/FSnote.wav","notes/A2note.wav"]

calEquation = ""

colorIndex = 0
windowHeight = 720
windowWidth = 1280
sizeOfColorChoices = 80
sizeOfmenuWindow = 170
sizeOfCalculator = 500
sizeOfCalButtons = 100
pressCalButton = True
choice = "paint"

fist_cascade = cv2.CascadeClassifier('fist.xml')

if fist_cascade.empty():
    print('WARNING: palm cascade did not load')

img = np.zeros((windowHeight,windowWidth,3), np.uint8)

'''
The SetMenu function creates the menu on the right side of the program which allows
the user to switch between the individuals applications inside FreeHand.
'''
def setMenu(img = img):
	cv2.rectangle(img,(windowWidth-sizeOfmenuWindow,0),(windowWidth, 100),(255,255,255),-1)
	cv2.putText(img, "Paint", (windowWidth-sizeOfmenuWindow+30,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)

	cv2.rectangle(img,(windowWidth-sizeOfmenuWindow,110),(windowWidth, 210),(255,255,255),-1)
	cv2.putText(img, "Piano", (windowWidth-sizeOfmenuWindow+30,170), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)

	cv2.rectangle(img,(windowWidth-sizeOfmenuWindow,220),(windowWidth, 320),(255,255,255),-1)
	cv2.putText(img, "Calculator", (windowWidth-sizeOfmenuWindow,280), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)
'''
SetColors function creates the different color options that appear in the left side
side of the paint app.
'''
def setColors():
    for i in range(9):
        cv2.rectangle(img,(0,sizeOfColorChoices*i),(sizeOfColorChoices*2, sizeOfColorChoices*i+sizeOfColorChoices), colors[i] ,-1)
'''
setCalculator function creates all the openCV labels that draw a simple calulator with Addition
Subtraction, Multiplication, and Division. It contains numbers from 0-9 as well as a C button to
restart the equation.
'''
def setCalculator():
    cv2.rectangle(img,(int(windowWidth/2-sizeOfCalculator/2), 0),(int(windowWidth/2+sizeOfCalculator/2), windowHeight-100),(0,255,0),2)
    cv2.rectangle(img,(int(windowWidth/2-sizeOfCalculator/2)+20, 20),(int(windowWidth/2+sizeOfCalculator/2)-20, sizeOfCalButtons),(0,255,0),2)
    cv2.cv2.putText(img, calEquation, (int(windowWidth/2-sizeOfCalculator/2)+20, sizeOfCalButtons-25), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    n = int(windowWidth/2-sizeOfCalculator/2)

    for y in range(4):
        for x in range(4):
            cv2.rectangle(img, (sizeOfCalButtons*x+20+(20*x)+n, sizeOfCalButtons*y+10+(20*y)+sizeOfCalButtons),(sizeOfCalButtons*x+sizeOfCalButtons+20+(20*x)+n, sizeOfCalButtons*y+sizeOfCalButtons+20+(20*y)+sizeOfCalButtons),(0,255,0),2)

    for i in range(3):
        cv2.putText(img, str(i+1), (n+50+ sizeOfCalButtons*i+(20*i), sizeOfCalButtons*2-10), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "+", (n+50+sizeOfCalButtons*3+(20*3), sizeOfCalButtons*2-25), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    for i in range(3):
        cv2.putText(img, str(i+4), (n+50+sizeOfCalButtons*i+(20*i), sizeOfCalButtons*3+10), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "-", (n+50+sizeOfCalButtons*3+(20*3)-5, sizeOfCalButtons*3), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    for i in range(3):
        cv2.putText(img, str(i+7), (n+50+sizeOfCalButtons*i+(20*i), sizeOfCalButtons*4+20), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "*", (n+50+sizeOfCalButtons*3+5+(20*3), sizeOfCalButtons*4+10), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "C", (n+30, sizeOfCalButtons*5+30), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(img, "0", (n+70+sizeOfCalButtons*1, sizeOfCalButtons*5+40), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(img, "=", (n+85+sizeOfCalButtons*2, sizeOfCalButtons*5+40), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(img, "/", (n+105+sizeOfCalButtons*3+10, sizeOfCalButtons*5+35), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2,cv2.LINE_AA)

def setPiano():
    cv2.rectangle(img,(0,0),(1100,450),(255,255,255),-1)

    for x in range(0,1200,110 ):
        cv2.rectangle(img,(0,0),(x,450),(0,0,0),0)
    for y in range(70,1170,110):
        if y==290 or y==730 or y==1060:
            continue
        cv2.rectangle(img,(y,0),(y+80,210),(0,0,0),-1)

def move(x,y):

    global colorIndex
    global choice
    global img
    global calEquation

    if x > windowWidth - sizeOfmenuWindow and y < 320:
        if y < 100:
            choice = "paint"
            img = np.zeros((windowHeight,windowWidth,3), np.uint8)
            setColors()
            setMenu(img)
        elif y < 210:
            choice = "piano"
            setPiano()
        elif y < 320:
            choice = "calculator"
            setCalculator()

    if choice is "paint":
        if x < sizeOfColorChoices*2:
            for i in range(9):
                if y < sizeOfColorChoices * i + sizeOfColorChoices:
                    colorIndex = i
                    break

    elif choice is "piano":
        pygame.init()
        counter=0
        counter2=0
        for i in range(0,1200,110):
            temp=i
            temp+=1
            temp2= i+70
            if (x>temp2 and x<temp2+80) and y<210 and x <1100:
                pygame.mixer.music.load(blackTones[counter2])
                pygame.mixer.music.play()
            elif (x<temp and i !=0) and (x>= i-110 and y<450) and x <1100:
                pygame.mixer.music.load(toneArray[counter])
                pygame.mixer.music.play()
            if counter ==6:
                counter=0
            else:
                counter+=1
            if counter2 ==4:
                counter2=0
            else:
                counter2+=1
    else:
        n = int(windowWidth/2-sizeOfCalculator/2)

        if(pressCalButton and x > 20+n and x < windowWidth/2+sizeOfCalculator/2-20 and y>sizeOfCalButtons+10 and y < sizeOfCalButtons*3+sizeOfCalButtons+20+(20*3)+sizeOfCalButtons):

            if y< sizeOfCalButtons*2+20:
                if x < n+sizeOfCalButtons+30:
                    calEquation += "1"
                elif x < n+sizeOfCalButtons*2+50:
                    calEquation += "2"
                elif x < n+sizeOfCalButtons*3+70:
                    calEquation += "3"
                elif x < n+sizeOfCalButtons*4+90:
                    calEquation += "+"
            elif y< sizeOfCalButtons*3+40:
                if x < n+sizeOfCalButtons+30:
                    calEquation += "4"
                elif x < n+sizeOfCalButtons*2+50:
                    calEquation += "5"
                elif x < n+sizeOfCalButtons*3+70:
                    calEquation += "6"
                elif x < n+sizeOfCalButtons*4+90:
                    calEquation += "-"

            elif y< sizeOfCalButtons*4+60:
                if x < n+sizeOfCalButtons+30:
                    calEquation += "7"
                elif x < n+sizeOfCalButtons*2+50:
                    calEquation += "8"
                elif x < n+sizeOfCalButtons*3+70:
                    calEquation += "9"
                elif x < n+sizeOfCalButtons*4+90:
                    calEquation += "*"

            elif y < sizeOfCalButtons*5+80:
                if x < n+sizeOfCalButtons+30:
                    calEquation = ""
                elif x < n+sizeOfCalButtons*2+50:
                    calEquation += "0"
                elif x < n+sizeOfCalButtons*3+70:
                    calEquation = str(eval(calEquation))
                elif x < n+sizeOfCalButtons*4+90:
                    calEquation += "/"
setMenu()

setColors()

cap = cv2.VideoCapture(0) #Change value to 1 if your device has more than 1 camera.

cap.set(3, 1200) #Sets the width of the cv2 window.
cap.set(4, 700) #Sets the height of the cv2 window.

pointX = 0
pointY = 0

while(1):
    ret, videoImg = cap.read()
    videoImg = cv2.flip(videoImg, 1)
''' gray gets the makes the video into a grayscale form in order for the fist to be recognized easier
    fist detects the actual fist from the gray variable. '''
    gray = cv2.cvtColor(videoImg, cv2.COLOR_BGR2GRAY)

    fist = fist_cascade.detectMultiScale(gray, 1.3,5)

    if choice is not "paint":
        img = videoImg
        setMenu(img)
        if(choice is "piano"):
            setPiano()
        else:
            setCalculator()
        for(x,y,w,h) in fist:
            pointX = x+int(w/2)
            pointY = y+int(h/2)
            move(pointX,pointY)

        if(pointX is -1):
            pressCalButton = True
        else:
            pressCalButton = False

    else:
        for(x,y,w,h) in fist:
            pointX = x+int(w/2)
            pointY = y+int(h/2)
            move(pointX,pointY)

    cv2.circle(img,(pointX,pointY),8, colors[colorIndex], -1)

    pointX = -1
    pointY = -1
    if cv2.waitKey(20) & 0xFF == 113:
        break

    cv2.imshow('image', img)

cv2.destroyAllWindows()
