# You should replace these 3 lines with the output in calibration step
import sys
from pathlib import Path

import cv2
import numpy as np

DIM=(2592, 1944)
K=np.array([[1278.5546532800213, 0.0, 1214.8485841051147], [0.0, 1280.6468268815097, 947.2420008999673], [0.0, 0.0, 1.0]])
D=np.array([[-0.01919372304232231], [-0.059736824909575006], [0.09502986266436268], [-0.055595195525532826]])
def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imwrite(str(Path(__file__).parents[1])+'/images/undisortet.jpg', undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
        undistort("file_to_undistort.jpg")