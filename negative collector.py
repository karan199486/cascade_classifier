import cv2
import os
import  urllib.request as ureq

path = "this is the path u want to save the images"

def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03259505'
    neg_images_urls = ureq.urlopen(neg_images_link).read().decode()

    global path
    path = 'c:/Users/karan/Desktop/neg'
    if not os.path.exists(path):
        os.makedirs(path)

    #count is used to name the images differently
    count = 910

    for i in neg_images_urls.split('\n'):
        try:
            print(i)
            ureq.urlretrieve(i,path+"/neg{}.jpg".format(count))
            img = cv2.imread(path+"/neg{}.jpg".format(count),cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img,dsize=(100,100))
            cv2.imwrite(path+"/neg{}.jpg".format(count),resized_image)
            count += 1

        except Exception as e:
            print(str(e))

store_raw_images()