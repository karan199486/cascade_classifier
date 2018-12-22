import os

dirpath = "c:/Users/karan/Desktop/stop sign detection"

try:
    bgtxtfile = open(dirpath+"/bg.txt", mode='w')

    for file in os.listdir(dirpath+'/negative'):
        bgtxtfile.write("negative/" + file + "\n")

    bgtxtfile.close()

except Exception as e:
    print(str(e))