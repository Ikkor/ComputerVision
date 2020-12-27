import cv2 
import numpy as np
import time


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

prev_frame_time = 0
  
# used to record the time at which we processed current frame 
new_frame_time = 0
  

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
        


        font                   = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (x,y)
        fontScale              = 1
        fontColor              = (0,255,0)
        lineType               = 2

        cv2.putText(img,'face', bottomLeftCornerOfText,font,fontScale,fontColor,lineType)



    #fps
    font = cv2.FONT_HERSHEY_SIMPLEX 
    # time when we finish processing for this frame 
    new_frame_time = time.time() 

    # Calculating the fps 

    # fps will be number of frame processed in given time frame 
    # since their will be most of time error of 0.001 second 
    # we will be subtracting it to get more accurate result 
    fps = 1/(new_frame_time-prev_frame_time) 
    prev_frame_time = new_frame_time 

    # converting the fps into integer 
    fps = int(fps) 

    # converting the fps to string so that we can display it on frame 
    # by using putText function 
    fps = str(fps) 

    # puting the FPS count on the frame 
    cv2.putText(img, 'FPS'+fps, (7, 70), font, 1, (100, 255, 0), 3, cv2.LINE_AA) 

    # displaying the frame with fps 
        
  




    cv2.imshow('img',img)
    print(img)
    k = cv2.waitKey(30) & 0xff

    if k==ord('q'):
        break
cap.release()