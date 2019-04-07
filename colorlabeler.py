import numpy as np
import cv2
class DetectImage :
   def __init__(self):
      pass
   def detectcolor(self,image) :
      hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
      red_lower = np.array([0,100,80],np.uint8)
      red_upper = np.array([10,255,255],np.uint8)
      blue_lower = np.array([110,50,50],np.uint8)
      blue_upper = np.array([130,255,255],np.uint8)
      green_lower = np.array([33,80,40],np.uint8)
      green_upper = np.array([102,255,255],np.uint8)
      red = cv2.inRange(hsv, red_lower, red_upper)
      blue = cv2.inRange(hsv, blue_lower, blue_upper)
      green = cv2.inRange(hsv, green_lower, green_upper)
      kernel = np.ones((5,5),'uint8')
      red = cv2.dilate(red,kernel)
      res = cv2.bitwise_and(image,image,mask = red)
      blue = cv2.dilate(blue,kernel)
      res = cv2.bitwise_and(image,image,mask = blue)
      green = cv2.dilate(green,kernel)
      res = cv2.bitwise_and(image,image,mask = green)
      (_,contours,hierachy) = cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      for pic,contour in enumerate(contours):
         area = cv2.contourArea(contour)
         if(area>300):
            M = cv2.moments(contour)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            cv2.putText(image, 'red',(cX-40,cY),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
      (_,contours,hierachy) = cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      for pic,contour in enumerate(contours):
         area = cv2.contourArea(contour)
         if(area>300):
            color = 'blue'
            M = cv2.moments(contour)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            cv2.putText(image, 'blue',(cX-40,cY),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
      (_,contours,hierachy) = cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      for pic,contour in enumerate(contours):
         area = cv2.contourArea(contour)
         if(area>300):
            color = 'green'
            M = cv2.moments(contour)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            cv2.putText(image, 'green',(cX-40,cY),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
 
      
            
        











