from pyrep import PyRep
import math
from pyrep.robots.arms.ur5 import UR5
from pyrep.robots.arms.ur5 import Arm
from pyrep.objects.shape import Shape
from pyrep.objects.dummy import Dummy
from pyrep import PyRep
from pyrep.objects.vision_sensor import VisionSensor
from pyrep.backend import sim
import numpy as np
import cv2

prevX = 0  # global variable
prevY = 0


def ballCoordinates(img):  # work with image format without imread
    global prevX
    global prevY
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img = img[450:962, 0:1024]  # region of interest
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # convert to hsv
    lower_red = np.array([0, 140, 140])
    upper_red = np.array([10, 255, 255])
    mask_red = cv2.inRange(imgHSV, lower_red, upper_red)  # binary mask put 1 if it  red in the image
    # get all non zero values
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(mask_red, connectivity=8)
    nb_components = nb_components - 1  # taking out the background which is also considered a componentbut
    Originx = 179
    Originy = 34
    if nb_components == 0:
        return "no ball"
    x = centroids[1][0] - Originx  # centert of coordinate x
    y = centroids[1][1] - Originy
    x = (x / 723) * 1.8
    y = (y / 352) * 0.9
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if prevX == 0 and prevY==0:  # first image to prev
        prevX = x
        prevY = y
        return [x, y]
    Vx = (x - prevX) / 0.05
    Vy = (y - prevY) / 0.05
    prevX = x
    prevY = y
    return [x, y], [Vx, Vy]


def Frame_ballCoordinates():
    x = cam.capture_rgb()  # type is float32
    x = np.uint8(x * 256)  # convert to uint8 and format of BGR
    target = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
    # lastTime = sim.simGetSimulationTime()
    # print(lastTime)
    print(ballCoordinates(target))
    pr.step()
    # return ballCoordinates(target)


SCENE_FILE = '/home/mishel/CoppeliaSim/scenes/Simulation.ttt'
pr = PyRep()
pr.launch(SCENE_FILE, headless=False)
pr.start()
cam = VisionSensor("cam")
ball = Shape('Sphere')
ballHandle=sim.simGetObjectHandle('Sphere')
pi = math.pi
agent = UR5()
# ball.set_position()
sim.simSetObjectFloatParameter(ballHandle,3001,3)
#sim.simSetObjectFloatParameter(ballHandle,3000,1)
while True:
     Frame_ballCoordinates()

pr.stop()
pr.shutdown()
