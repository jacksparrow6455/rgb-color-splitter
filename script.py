#Importing Libraries
import cv2
import numpy as np

#Start Using Camera Feed to record frames (set to 0 for default camera, set to 1 for external camera(webcam))
cam=cv2.VideoCapture(0)
while True:
    #Reading frames
    ret,frame=cam.read()
    
    #Converting frame into hsv format for analysis
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #Defining Ranges for Blue, Green and Red color(hsv)
    lower_range_blue=np.array([110,50,50])
    upper_range_blue=np.array([130,255,255])
    
    lower_range_green=np.array([40,100,100])
    upper_range_green=np.array([80,255,255])
    
    lower_range_red=np.array([0,100,100])
    upper_range_red=np.array([40,255,255])
    
    #Creating a mask for each color and separating out color
    red=cv2.inRange(hsv,lower_range_red,upper_range_red)
    result_red=cv2.bitwise_and(frame,frame,mask=red)
    
    blue=cv2.inRange(hsv,lower_range_blue,upper_range_blue)
    result_blue=cv2.bitwise_and(frame,frame,mask=blue)
    
    green=cv2.inRange(hsv,lower_range_green,upper_range_green)
    result_green=cv2.bitwise_and(frame,frame,mask=green)
    
    #Displaying frames using 4 different windows
    cv2.imshow("Red Identifier",result_red)
    cv2.imshow("Green Identifier",result_green)
    cv2.imshow("Blue Iddentifier",result_blue)
    cv2.imshow("Live Feed",frame)
    
    #Setting escape key to close all windows
    if cv2.waitKey(1)==27:
        break

#Releasing the Camera
cam.release()
cv2.destroyAllWindows()