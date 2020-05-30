import cv2
import numpy as np
import PIL
#from PIL import Image


def makeGrey(imagePath):
    imgGrey = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    return imgGrey

def trueBlackWhite(path,thresh,finalPath):
    imgGrey = makeGrey(path)
    th = cv2.threshold(imgGrey, thresh, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite(finalPath, th)
    return th

def setSliderVal(self,sliderVal):
    self.sliderVal=sliderVal

def update(self):
    self.toUpdate

def clearImg(imagePath):
    blank_image2 = 255 * np.ones(shape=[512, 512, 3], dtype=np.uint8)
    cv2.imwrite(imagePath, blank_image2, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

def scaleImgKeepAspectRatio(img, scalePercent):
    width = int(img.shape[1] * scalePercent / 100)
    height = int(img.shape[0] * scalePercent / 100)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

def resizeImg(img, width, height):
    dim = (int(width), int(height))
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

def pil2Cv(img):
    return np.asarray(img)

def cv2Pil(img,path):
    cv2.imwrite(path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])  # Sch
    img = PIL.Image.open(path)
    return img

def writeImgToFile(img, path):
    try:
        cv2.imwrite(path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])  # Sch
    except:
        img.save(path, "JPEG")

        #self.imgRoot + '/07.jpg'