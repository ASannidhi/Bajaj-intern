import cv2
import numpy as np

def zoom_center(fig, zoom_factor=2.2):

    y_size = fig.shape[0]
    x_size = fig.shape[1]
    
    # define new boundaries
    x1 = int(0.5*x_size*(1-1/zoom_factor))
    x2 = int(x_size-0.5*x_size*(1-1/zoom_factor))
    y1 = int(0.5*y_size*(1-1/zoom_factor))
    y2 = int(y_size-0.5*y_size*(1-1/zoom_factor))

    # first crop image then scale
    img_cropped = fig[y1:y2,x1:x2]
    return cv2.resize(img_cropped, None, fx=zoom_factor, fy=zoom_factor)

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,780)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1270)
cv2.namedWindow("camera test")
img_counter=0

while True:
    ret,frame=cap.read()
    mask = np.zeros(frame.shape[:2], dtype="uint8")
    cv2.circle(mask, ( 392, 281), 24, 255, -1)
    masked = cv2.bitwise_and(frame, frame, mask=mask)
    
    #blurimg = cv2.GaussianBlur(masked,(5,5), 1)
    #blurimg = cv2.medianBlur(masked,5)
    blurimg = cv2.bilateralFilter(masked,2,75,75)
    imageGray = cv2.cvtColor(blurimg, cv2.COLOR_RGB2GRAY)
    #img_zoomed_and_cropped = imageGray[235:335, 345:445]
    img_zoomed_and_cropped = zoom_center(imageGray)
    
    
    circles = cv2.HoughCircles(img_zoomed_and_cropped ,cv2.HOUGH_GRADIENT,1,21,param1=50,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
    # draw the outer circle
        cv2.circle(img_zoomed_and_cropped,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
        #cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)


    k = cv2.waitKey(1)
    if k%256 == 27:
        print('Escape hit. Closing...')
        break
    elif k%256 == 32:
        img_name = "imagelight_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written".format(img_name))
        img_counter += 1       
    cv2.imshow("camera test",img_zoomed_and_cropped)
cap.release()
cv2.destroyAllWindows()    