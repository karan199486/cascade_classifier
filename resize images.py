import cv2
import os

path = "c:/Users/karan/Desktop/gui training/p"

sample_h = 50
sample_w = 50

for filename in os.listdir(path):
    img = cv2.imread(path+"/"+filename)

    imgh = img.shape[0]
    imgw = img.shape[1]
    ratio = imgw/imgh

    if imgw >= imgh:
        imgw = sample_w
        imgh = int(imgw / ratio)

    else:
        imgh = sample_h
        imgw = int(imgh * ratio)

    #print(imgh,imgw)
    img = cv2.resize(src=img,dsize=(imgw,imgh))

    cv2.imwrite(path+"/"+filename,img)

    print("successfully resized")