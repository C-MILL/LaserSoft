from pathlib import Path

import PIL
import cv2
from PIL import Image

from ImageManipulation.ImageEditing import writeImgToFile


def convertImageToPrintableDict(img):
    imgRoot = str(Path(__file__).parents[1]) + '/images'
    height, width = img.shape
    # img = cv2.flip(img, 0)
    writeImgToFile(img, imgRoot + '/10.jpg')
    first=False
    dict={'x':[],'y':[],'laser':[]}
    reversedDict={'x':[],'y':[],'laser':[]}
    for column in range(height):
        for row in range(width):
            if img[column][row]<150: #then black
                if first==False:
                    first=True
                    if row<width-1: #if there is a next pixel:
                        if img[column][row+1]>150: #if next pixel is not Black too,
                            # go to this pixel
                            dict=appendToList(dict,row, column, False)
                            # now print on next one
                            dict=appendToList(dict,row+1, column, True)
                        else: #next pixel is black too
                            #go to current position
                            dict = appendToList(dict, row, column, False)
                    else: #if there is no next pixel:
                        # go to pixel before
                        dict=appendToList(dict,row-1, column, False)
                        # now print on current
                        dict=appendToList(dict,row, column, True)
                else: #not first black pixel
                    if row<width-1: #if there are more pixels
                        if img[column][row+1]>150: #if next pixel is not black too
                            #print until current
                            dict=appendToList(dict,row,column,True)
                    else: #last pixel
                        #print until current
                        dict=appendToList(dict,row, column, True)
            else:
                first=False

    return dict

def appendToList(dict,row, column, laser):
    dict['x'].append(row)
    dict['y'].append(column)
    dict['laser'].append(laser)
    return dict





# imgRoot = str(Path(__file__).parents[1]) + '/images'
# img = cv2.imread(imgRoot + '/01.jpg')
# convertImageToPrintableDict(img)