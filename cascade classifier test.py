# to detect objects in images in a folder

import cv2
import os

cascadepath = 'c:/Users/karan/Desktop/stop sign detection/data/cascade.xml'     #cascade xml file path

classifier = cv2.CascadeClassifier(cascadepath)

path = 'c:/Users/karan/Desktop/rawdata'

for file in os.listdir(path):
    img = cv2.imread(path+"/"+file)
    cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    dim = classifier.detectMultiScale(img)

    for x,y,w,h in dim:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),color=(255,0,0))
        cv2.putText(img,text="stop",org=(x+10,y-10),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1.5,color=(0,0,255),thickness=2,lineType=cv2.LINE_AA)
    cv2.imshow("",img)
    cv2.waitKey()

cv2.destroyAllWindows()