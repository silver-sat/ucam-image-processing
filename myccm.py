# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:33:31 2021

@author: Nathan
"""

import numpy as np
import cv2

def gamma_correction(rgb, gamma=2.2):
    arr = rgb.copy()
    mask = (rgb>=0)
    arr[mask] = np.power(arr[mask], gamma)
    arr[~mask] = -np.power(-arr[~mask], gamma)
    return arr

def gamma_correction_undo(rgb, gamma=2.2):
    arr = rgb.copy()
    mask = (rgb>=0)
    arr[mask] = np.power(arr[mask], 1/gamma)
    arr[~mask] = -np.power(-arr[~mask], 1/gamma)
    return arr

class MLRCCM(object):
    def __init__(self,src,dst):
        self._ccm = self._compute(src,dst)
    
    def _compute(self,x,y):
        beta = np.linalg.lstsq(x,y,rcond=None)[0]
        print(beta)
        return beta
    
    def _infer(self,ccm,img):
        return np.matmul(img, ccm)
    
    def infer_image(self,imgfile):
        img = cv2.imread(imgfile)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
        out = self._infer(self._ccm,img)
        img = np.minimum(np.maximum(np.round(out*255), 0), 255)
        img = img.astype(np.uint8)
        return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
class MLRCCMGamma(MLRCCM):
    def __init__(self,src,dst,gamma=2.2):
        self._gamma = gamma
        self._ccm = self._compute(gamma_correction(src,self._gamma),
                                  gamma_correction(dst,self._gamma))
    
    def infer_image(self,imgfile):
        img = cv2.imread(imgfile)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
        out = self._infer(self._ccm,gamma_correction(img,self._gamma))
        out = gamma_correction_undo(out,self._gamma)
        img = np.minimum(np.maximum(np.round(out*255), 0), 255)
        img = img.astype(np.uint8)
        return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        
            

            
    
        
        