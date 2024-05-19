import cv2
import os

path = "C:/Pankil/Python/Projects/P105-videomaking/Images"

images=[]

for file in os.listdir(path):
    name,ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        fileName = path + "/" + file
        print(fileName)

    images.append(fileName)

count = len(images)

frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)
out = cv2.VideoWriter("friends.mp4",cv2.VideoWriter_fourcc(*'DIVX'),1,size)

for image in range(0,count-1):
    frame = cv2.imread(images[image])
    out.write(frame)

out.release()