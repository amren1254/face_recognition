import cv2
import numpy as np
import os


cap = cv2.VideoCapture(0)

id=input("Enter id number for user")
user = input("Enter user name")
#os.mkdir(user)
samplenumber=0
##cv2.waitKey(300)

while True:
    re, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = model.detectMultiScale(gray,1.7,5)

    for x,y,w,h in faces:
        samplenumber=samplenumber+1
        cv2.imwrite("dataset/user." + str(id) +"."+str(samplenumber)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),5)
        
        cv2.waitKey(300);
        

    cv2.imshow('DataSet For Training Of Data',frame)
    cv2.waitKey(1)
    if samplenumber>15:
        break
    
cap.release()
cv2.destroyAllWindows()


