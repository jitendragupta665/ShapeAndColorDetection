from colorlabeler import DetectImage
from shapedetector import ShapeDetector
import cv2
import numpy as np
img = cv2.imread('test1.png')
h,w,c = img.shape
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)
thres = cv2.threshold(blurred,220,255,1)[1]
cnts = cv2.findContours(thres, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[1]
sd = ShapeDetector()
cl = DetectImage()
list1 = ['tes1.png']
for c in cnts :
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    shape = sd.detect(c,h)
    color = cl.detectcolor(img)
    list1.append([color,shape])
    cv2.drawContours(img,[c],-1,(0,0,0),2)
    cv2.putText(img, shape, (cX+10,cY),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0), 2)
print(list1)
cv2.imshow('image',img)
cv2.waitKey(0)

 
