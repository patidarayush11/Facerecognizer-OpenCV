import cv2
import sqlite3

def insertOrUpdate(id,name):
    conn = sqlite3.connect('database.db')
    cmd="SELECT * FROM People Where ID="+str(id)
    cursor=conn.execute(cmd)
    isRecord=0
    for row in cursor:
        isRecord=1
    if(isRecord==1):
        cmd="UPDATE People SET Name="+str(name)+" WHERE ID="+str(id)
    else:
        cmd="INSERT INTO People(ID,Name) Values("+str(id)+","+str(name)+")"
    print cmd
    conn.execute(cmd)
    conn.commit()
    conn.close()



cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('Classifiers/face.xml')
i=0
offset=0
id=raw_input('enter your ID : ')
name=raw_input('enter your Name : ')
insertOrUpdate(id,name)
while True:
    c=raw_input("Enter y to click a picture : ")
    if(c=="y"):
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        for(x,y,w,h) in faces:
            i=i+1
            cv2.imwrite("dataSet/"+id +'.'+str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
            cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
            cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
            cv2.waitKey(10)
            if i>40:
                cam.release()
                cv2.destroyAllWindows()
                break
    else:
        print("Invalid input")

