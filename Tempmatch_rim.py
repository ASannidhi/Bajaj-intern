import cv2

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,780)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1270)
cv2.namedWindow("camera test")
img_counter=0

img1=cv2.imread(r"C:\Users\asannidhi\Desktop\tempimg_mattred.png")
template1 = img1[50:200,200:600]
img2=cv2.imread(r"C:\Users\asannidhi\Desktop\tempimg_glossyred.png")
template2 = img2[50:200,200:600]
img3=cv2.imread(r"C:\Users\asannidhi\Desktop\tempimg_plasmablue.png")
template1 = img3[50:200,200:600]
while True:
    ret,frame=cap.read()
    top_left=(180,45)
    bottom_right=(620,220)
    cv2.rectangle(frame,top_left, bottom_right, 255, 2)
    areacov = frame[45:220, 180:620]
    imageGray = cv2.cvtColor(areacov, cv2.COLOR_RGB2GRAY)
    ret1,thresh1 = cv2.threshold(imageGray,100,255,cv2.THRESH_BINARY)
    
    templateGray1 = cv2.cvtColor(template1, cv2.COLOR_RGB2GRAY)
    ret21,thresh21 = cv2.threshold(templateGray1,100,255,cv2.THRESH_BINARY)
    templateGray2 = cv2.cvtColor(template2, cv2.COLOR_RGB2GRAY)
    ret22,thresh22 = cv2.threshold(templateGray2,100,255,cv2.THRESH_BINARY)
    templateGray3 = cv2.cvtColor(template3, cv2.COLOR_RGB2GRAY)
    ret23,thresh23 = cv2.threshold(templateGray3,100,255,cv2.THRESH_BINARY)
    
    result = cv2.matchTemplate(thresh1, thresh21, cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    #format_maxVal = "{:.2f}".format(maxVal)
    #print(format_maxVal)
    print(maxVal)
    probval = 0.865
    if maxVal>=probval:
        cv2.putText(frame, "PRESENT", (300,500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1)

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