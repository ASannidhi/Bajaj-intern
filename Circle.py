import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

videocapture = cv.VideoCapture(0)
while(True):
    ret, frame = videocapture.read()
    if not ret: break
   # cv.imshow("test",frame)
    img=frame.copy()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (9,9),0)
    minDist = 1
    param1 = 30 #500
    param2 = 50 #200 
    minRadius = 5
    maxRadius = 100 #10
    
    circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 1.2, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            r_mm = 
            cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2) 
      #  cv.circle(img, (i[0], i[1]), 2, (0,0,255), 2 ) -->this is for plotting centre
    cv.imshow('img',img)
    if cv.waitKey(1) & 0xFF == ord('q'): break
    
videocapture.release()
cv.destroyAllWindows()