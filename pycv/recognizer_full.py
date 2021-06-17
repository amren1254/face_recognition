import cv2
import numpy as np
import csv

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

#data = []
#read = csv.reader(open("d1.csv"))
#for row in read:
#    data.append(row)
#

cam = cv2.VideoCapture(0)
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (0, 255, 0)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),4)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        a=Id
        if(conf<50):
            if(Id==1):
                Id="Amrendra"
            elif(Id==2):
                Id="Shivam"
        else:
            Id="Unknown"
        cv2.putText(im,str(Id), (x,y+h),font, 1,fontcolor)
    cv2.imshow('Attendance Window',im) 
    if cv2.waitKey(1) == ord('q'):
            break
f1=open("attendance_sheet.csv",'a')
f1.write(str(a))
f1.write(",")
f1.write(data[a][0])
f1.write(",")
f1.write(time.ctime())
f1.write("\n")
cam.release()
cv2.destroyAllWindows()
