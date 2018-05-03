import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# windowHeight = 1280
# windowWidth = 1024
# cap.set(3,windowHeight)
# cap.set(4, windowWidth)

# def draw_circle(event,x,y,flags,param):
#
#     global color
#
#     if x > windowWidth-100:
#         if y < 108:
#             color = (0, 255, 0)
#         elif y < 218:
#             color = (0, 0, 255)
#
#     if event == cv2.EVENT_MOUSEMOVE:
#         cv2.circle(img,(x,y),8, color, -1)
# img = np.zeros((windowHeight,windowWidth,3), np.uint8)
# cv2.setMouseCallback('regular', draw_circle)
# cv2.rectangle(img,(windowWidth-100,0),(windowWidth,108),(0,255,0),-1)
# cv2.rectangle(img,(windowWidth-100,108),(windowWidth,218),(0,0,255),-1)
#creating camera object
while( cap.isOpened() ):
    ret, img = cap.read() #reading the frames
    # cv2.imshow('regular', vid) #displaying the frames
    gray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh1 = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # cv2.setMouseCallback('countour', draw_circle)
    img, contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if(area > max_area):
            max_area = area
            ci = i
    cnt = contours[ci]
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(img.shape, np.uint8)
    cv2.drawContours(drawing, [cnt], 0, (0,255,0), 2)
    cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 2)

    cv2.imshow('contour', thresh1)
    k = cv2.waitKey(10)
    if k == 27:
       break
