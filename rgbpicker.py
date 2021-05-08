# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 17:03:56 2021

@author: Nathan
"""

import cv2
import numpy as np

photofile = "ColorTest_Phone_compressed.jpg"
# photofile = "ColorTest_uCAMIII.jpg"
# photofile = "ColorTest_original.jpg"

#this function will be called whenever the mouse is right-clicked
def mouse_callback(event, x, y, flags, params):
    global region
    if event == 1:
        # left-click
        # print(event,x,y,flags,params)
        s = np.zeros((3,)); c = 0;
        for xi in range(x-5,x+5):
            for yi in range(y-5,y+5):
                s += img[yi][xi]
                c += 1
        s = s/c
        print (region,"%02X"%int(round(s[2])),
                      "%02X"%int(round(s[1])),
                      "%02X"%int(round(s[0])))
        region+=1
 
region = 0
img = cv2.imread(photofile)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

scale_width = 640 / img.shape[1]
scale_height = 480 / img.shape[0]
scale = min(scale_width, scale_height)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', window_width, window_height)

#set mouse callback function for window
cv2.setMouseCallback('image', mouse_callback)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()