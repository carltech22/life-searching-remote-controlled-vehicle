import numpy as np
import cv2

cap=cv2.VideoCapture("Facial_Recognition_Test1.mp4")
#cap.set(cv2.CAP_PROP_FPS, 10000)
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    font=cv2.FONT_HERSHEY_SIMPLEX
    width=int(cap.get(3))
    height=int(cap.get(4))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
        roi_gray=gray[y:y+w,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(0,255,0),5)
            frame=cv2.putText(frame,'Survivor Detected',(10,height-40),font,2,(255,25,255),3,cv2.LINE_AA)


    cv2.imshow('frame',frame)
    if cv2.waitKey(25)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
