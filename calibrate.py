# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 16:49:58 2021

@author: Nathan
"""

import cv2
from swatches import reference, uCAM, phone

reffname = "ColorTest_original.jpg"
uCAMfname = "ColorTest_uCAMIII.jpg"
phonefname = "ColorTest_Phone_compressed.jpg"

reffn = reffname
refsw = reference

srcfn = uCAMfname
srcsw = uCAM

# srcfn = phonefname
# srcsw = phone

# srcfn = reffname
# srcsw = reference

refimg = cv2.imread(reffn)
photoimg = cv2.imread(srcfn)

def showimage(name,img):
    scale_width = 640 / img.shape[1]
    scale_height = 480 / img.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(img.shape[1] * scale)
    window_height = int(img.shape[0] * scale)
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, window_width, window_height)
    cv2.imshow(name, img)
    
from color_calibration.api import color_calibration
from color_calibration import color

ccm = color_calibration(src=srcsw,dst=color.Color(refsw,color.sRGB))
correctedimg = ccm.infer_image(srcfn)

from myccm import MLRCCM, MLRCCMGamma
ccm1 = MLRCCM(srcsw,refsw)
myccmimg1 = ccm1.infer_image(srcfn)
ccm2 = MLRCCMGamma(srcsw,refsw,gamma=2.5)
myccmimg2 = ccm2.infer_image(srcfn)

from skimage import exposure

histphotoimg = exposure.match_histograms(photoimg, refimg, multichannel=True)

cv2.imwrite(srcfn.rsplit('.',1)[0]+".corrected.jpg",correctedimg)
cv2.imwrite(srcfn.rsplit('.',1)[0]+".myccm1.jpg",myccmimg1)
cv2.imwrite(srcfn.rsplit('.',1)[0]+".myccm2.jpg",myccmimg2)
cv2.imwrite(srcfn.rsplit('.',1)[0]+".histcorr.jpg",histphotoimg)

showimage("reference",refimg)
showimage("photo",photoimg)
showimage("corrected",correctedimg)
showimage("myccm1",myccmimg1)
showimage("myccm2",myccmimg2)
showimage("histcorr",histphotoimg)

cv2.imwrite(srcfn.rsplit('.',1)[0]+".corrected.jpg",correctedimg)


cv2.waitKey(0)
cv2.destroyAllWindows()
