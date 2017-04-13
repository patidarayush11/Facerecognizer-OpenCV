import cv2,os
import numpy as np
from PIL import Image 
import pickle
import sqlite3

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainner/trainner.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'

def getProfile(id):
    conn = sqlite3.connect('database.db')
    cmd="SELECT * FROM People Where ID="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, .5, 0, 2, 1) #Creates a font
profiles={}
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        profile=getProfile(nbr_predicted)
        print profile
        if(profile!=None):
            cv2.cv.PutText(cv2.cv.fromarray(im),"Name:"+str(profile[1]), (x,y+h+20),font, (0,0,255)) #Draw the text
            cv2.cv.PutText(cv2.cv.fromarray(im),"Age:"+str(profile[2]), (x,y+h+50),font, (0,0,255)) #Draw the text
            cv2.cv.PutText(cv2.cv.fromarray(im),"Gender:"+str(profile[3]), (x,y+h+80),font, (0,0,255)) #Draw the text
            cv2.cv.PutText(cv2.cv.fromarray(im),"Registration Number:"+str(profile[4]), (x,y+h+110),font, (0,0,255)) #Draw the text
    cv2.imshow('im',im)
    cv2.waitKey(10)
















    
