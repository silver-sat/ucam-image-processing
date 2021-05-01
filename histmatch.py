# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 17:03:56 2021

@author: Nathan
"""

import cv2

def showimage(name,img):
    scale_width = 640 / img.shape[1]
    scale_height = 480 / img.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(img.shape[1] * scale)
    window_height = int(img.shape[0] * scale)
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, window_width, window_height)
    cv2.imshow(name, img)

import numpy as np

matrix = np.array([[ 2.47208496e+00,-1.01904253e+00,-9.34519430e-01,1.88586085e+02],
                   [-4.19752400e-01,2.67233939e+00,-7.42100369e-01,5.96648759e+01],
                   [ 7.60589434e-01,-1.34789757e-01,1.31854856e+00,-1.54574396e+02]])

matrix = np.array([[ 2.70722745,-0.32371901,-0.4076851 ],
                   [-0.34535801, 2.89232588,-0.5754205 ],
                   [ 0.56785513,-0.70471098, 0.88672933]])

matrix = np.array([[ 1.90087624,-0.9840015,0.07211266],
                   [-1.37759033,2.03872528,0.03974277],
                   [ 0.02764763,-1.1621579,1.20894387]])

matrix = np.array([[0.22765575, 0.10881795, 0.28157732],
                   [0.10296851, 0.36147478, 0.20198812],
                   [0.30029102, 0.24406538, 0.74480083]])

matrix = np.array([[ 2.04861930e+00, -1.54225476e+00, -9.18225758e-01,2.55183141e+02],
                   [-1.26507259e+00,  1.61357233e+00, -7.14476378e-01,1.94341660e+02],
                   [ 8.58681564e-03, -1.09013582e+00,  1.33671066e+00,-3.29220104e+01]])

def trans(img):
    img1 = img.copy()
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            for k in range(3):
                newval = np.dot(img1[i,j],matrix[k,:3]) + matrix[k,3]
                # newval = np.dot(img1[i,j],matrix[k,:3])
                img1[i,j,k] = min(max(newval,0),255)
    return img1
        
img1 = cv2.imread(r"c:\Users\Nathan\Downloads\ColorTest_original.jpg")
img2 = cv2.imread(r"c:\Users\Nathan\Downloads\ColorTest_uCAMIII.jpg")

showimage("reference",img1)
showimage("photo",img2)

from skimage import exposure

img3 = exposure.match_histograms(img2, img1, multichannel=True)
img4 = trans(img2)

showimage("corrected",img3)
showimage("trans",img4)

cv2.waitKey(0)
cv2.destroyAllWindows()