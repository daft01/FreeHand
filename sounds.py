import numpy as np
import cv2
import tkinter
from playsound import playsound
import pygame

cv2.namedWindow('Piano')
#height 600 width 1500
img = np.zeros((600,1200,3), np.uint8)

toneArray= ["Anote.wav","Bnote.wav","Cnote.wav","Dnote.wav","Enote.wav","Fnote.wav","Gnote.wav"]
blackTones=["AFnote.wav","CSnote.wav","DSnote.wav","FSnote.wav","A2note.wav"]

def sound_make(event,x,y,flags,prameters):
    pygame.init()
    counter=0
    counter2=0
    for i in range(0,1200,110):
        temp=i
        temp+=1
        temp2= i+70
        if event ==cv2.EVENT_LBUTTONDOWN:
            if (x>temp2 and x<temp2+80) and y<210:
                pygame.mixer.music.load(blackTones[counter2])
                pygame.mixer.music.play()
            elif (x<temp and i !=0) and (x>= i-110 and y<450):
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

cv2.rectangle(img,(0,0),(1200,600),(255,255,255),-1)

for x in range(0,1200,110 ):
    cv2.rectangle(img,(0,0),(x,450),(0,0,0),0)
for y in range(70,1170,110):
    if y==290 or y==730 or y==1060:
        continue
    cv2.rectangle(img,(y,0),(y+80,210),(0,0,0),-1)
    print(y)





# font = cv2.FON    T_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.setMouseCallback('Piano', sound_make)
while(1):
    cv2.imshow('Piano',img)
    if cv2.waitKey(20) & 0xFF == 113:
        break

cv2.destroyAllWindows()

