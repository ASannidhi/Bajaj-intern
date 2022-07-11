import cv2 as cv
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def grab_frame(cap):
    ret,frame = cap.read()
    return cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

cap1 = cv2.VideoCapture(0)
#cap2 = cv2.VideoCapture(1)

#create two subplots
ax1 = plt.subplot(1,1,1)
#ax2 = plt.subplot(1,2,2)

#img_path="opencv_frame_0.png"
#img=cv.imread(img_path)

#create two image plots
im1 = ax1.imshow(grab_frame(cap1))
#im2 = ax2.imshow(grab_frame(cap2))

def update(i):
    im1.set_data(grab_frame(cap1))
    #im2.set_data(grab_frame(cap2))
    
ani = FuncAnimation(plt.gcf(), update, interval=200)
plt.show()
