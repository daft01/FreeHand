import numpy as np
import cv2
import tkinter
from playsound import playsound
import pygame

cv2.namedWindow('Piano')
img = np.zeros((512,512,3), np.uint8)

toneArray= ["Anote.wav","Bnote.wav","Cnote.wav","Dnote.wav","Enote.wav","Fnote.wav","Gnote.wav"]
blackTones=["AFnote.wav","CSnote.wav","DSnote.wav","FSnote.wav","A2note.wav"]

def sound_make(event,x,y,flags,prameters):
    counter=5
    counter2=3
    for i in range(0,512,46):
        temp=i
        temp+=1
        temp2= i+30
        if event ==cv2.EVENT_LBUTTONDOWN:
            if x>temp2 and x<temp2+32 and y<58:
                pygame.init()
                pygame.mixer.music.load(blackTones[counter2])
                pygame.mixer.music.play()
            elif x<temp and i !=0 and x>= i-46 and y<128:
                pygame.init()
                pygame.mixer.music.load(toneArray[counter])
                pygame.mixer.music.play()
        if counter ==6:
            counter=0
        else:
            counter+=1
        if counter2 ==4:
            counter=0
        else:
            counter2+=1

for x in range(0,512,46):
    cv2.rectangle(img,(0,0),(x,128),(255,255,255),2)
for y in range(30,482,46):
    if(y==168 or y==306):
        continue
    cv2.rectangle(img,(y,0),(y+32,58),(0,0,255),2)
    print(y)





# font = cv2.FON    T_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.setMouseCallback('Piano', sound_make)
while(1):
    cv2.imshow('Piano',img)
    if cv2.waitKey(20) & 0xFF == 113:
        break

cv2.destroyAllWindows()
