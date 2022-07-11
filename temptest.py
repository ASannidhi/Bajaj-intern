import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

videocapture = cv.VideoCapture(0)
while(True):
    ret, frame = videocapture.read()
    if not ret: break
    #cv.imshow("test",frame)
    img=frame.copy()
    
    ROI= np.array([[(260,285),(260,195),(365,195),(365,285)]], dtype= np.int32)
    top_left = (260,195)
    bottom_right = (365,285)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    crop=img[195:285, 260:365]
    temp_path="savedImage1.png"
    template = cv.imread(temp_path)
    #methods = ['cv.TM_CCOEFF_NORMED']
    #for meth in methods:
        #img1 = img.copy()
        #method = eval(meth)
    # Apply template Matching
    method = eval('cv.TM_CCOEFF_NORMED')
    res = cv.matchTemplate(img,template,method )
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    
    plt.imshow(img,cmap = 'gray')    
    #print(max_val)
    if cv.waitKey(1) & 0xFF == ord('q'): break

videocapture.release()
cv.destroyAllWindows()