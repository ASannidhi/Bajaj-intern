import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

videocapture = cv.VideoCapture(0)
while(True):
    ret, frame = videocapture.read()
    if not ret: break
    cv.imshow("test",frame)
    if cv.waitKey(1) & 0xFF == ord('q'): break

videocapture.release()
cv.destroyAllWindows()