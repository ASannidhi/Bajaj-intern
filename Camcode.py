import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,780)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1270)
cv2.namedWindow("camera test")
img_counter=0
while True:
    ret,frame=cap.read()
    k = cv2.waitKey(1)
    if k%256 == 27:
        print('Escape hit. Closing...')
        break
    elif k%256 == 32:
        img_name = "imagelight_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written".format(img_name))
        img_counter += 1       
    cv2.imshow("camera test",frame)
cap.release()
cv2.destroyAllWindows()    