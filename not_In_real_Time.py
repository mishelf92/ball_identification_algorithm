import cv2
import numpy as np
import time
import csv

prevX = 0
prevY = 0


def ballCoordinates(image):
    global prevX
    global prevY
    img = cv2.imread(image)
    img = img[0:600, 0:2000]  # region of interest
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # convert to hsv
    lower_red = np.array([0, 140, 140])
    upper_red = np.array([10, 255, 255])
    mask_red = cv2.inRange(imgHSV, lower_red, upper_red)  # binary mask put 1 if it  red in the image
    # get all non zero values
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(mask_red, connectivity=8)
    nb_components = nb_components - 1  # taking out the background which is also considered a componentbut
    Originx = 116
    Originy = 182
    if nb_components == 0:
        return "no ball"
    x = centroids[1][0] - Originx  # centert of coordinate x
    y = centroids[1][1] - Originy
    if prevX == 0:# first image to prev
        prevX = x
        prevY = y
       # return [x,y]
    Vx = (x - prevX) / 0.05
    Vy = (y - prevY) / 0.05
    prevX = x
    prevY = y

    with open('AlgorithmLabels.csv', 'a', newline='') as file:
         writer = csv.writer(file)
         writer.writerow([x,y])

    return [x,y], [Vx,Vy]





for i in range(17):
   # print(ballCoordinates("image " + str(i + 1) + ".png"))
   ballCoordinates("image " + str(i + 1) + ".png")


#print(time.time() - start)