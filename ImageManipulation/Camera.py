from pathlib import Path
import platform
if platform.machine()!='x86_64':
    from picamera import PiCamera
from time import sleep
import cv2

from ImageManipulation.undisort import undistort


def cameraTest(state):
    print(state)
def camera(config,camera):
    imgRoot=str(Path(__file__).parents[1])+'/images'
    if platform.machine() != 'x86_64':
        camera.capture(imgRoot+'/camImage.jpg')
    sleep(1)
    undistort(str(Path(__file__).parents[1])+'/images/camImage.jpg')
    image = cv2.imread(str(Path(__file__).parents[1])+'/images/undisortet.jpg')
    width=config['camWidth']
    height=config['camHeight']
    offX=config['camOffsetX']
    offY=config['camOffsetY']
    cropped = image[offY:height+offY, offX:width+offX]
    x=cropped.shape[1]
    y=cropped.shape[0]
    if x/6>y/4:
        r = 600.0 / x
        dim = (600, int(y * r))
    else:
        r=400/y
        dim = (int(x * r),400)
    resized = cv2.resize(cropped, dim, interpolation=cv2.INTER_AREA)
    rotatedImg = cv2.rotate(resized, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(str(Path(__file__).parents[1])+'/images/finalCamImage.jpg', rotatedImg)
    
