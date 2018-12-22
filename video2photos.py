import cv2

cap = cv2.VideoCapture('c:/Users/karan/Desktop/video.mp4')   # video file path

count = 1
num = 1

while cap.isOpened():
    res,img = cap.read()

    if res == False:
        break

    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    img = cv2.resize(src=img,dsize=(320,240))

    if count % 5 == 0:
        cv2.imwrite("c:/Users/karan/Desktop/negative/"+str(num)+".jpg",img)   # path where you want to save your images
        num += 1

    count += 1

cap.release()
