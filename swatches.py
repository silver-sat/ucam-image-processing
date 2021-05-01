# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 16:18:39 2021

@author: Nathan
"""

__all__ = [ "uCAM" , "phone", "reference"]

import numpy as np

uCAM_swatches = """
0 FF B3 97
1 FF 32 4D
2 85 64 15
3 74 3C 3E
4 C4 4E 40
5 FF BB 5E
6 75 67 67
7 FF 46 7F
8 82 1C 10
9 FF 3F 66
10 84 63 14
11 54 2C 34
12 F1 89 6E
13 FF B9 5F
14 7D 6E 69
15 FF 41 7C
"""

phone_swatches = """
0 CA C6 C3
1 B7 38 32
2 41 7B 48
3 34 52 9A
4 77 58 5D
5 C1 A1 26
6 1A 86 BF
7 C2 48 7B
8 46 33 34
9 C3 3D 37
10 35 6D 3C
11 28 4E 97
12 B3 A5 A5
13 D8 BF 2F
14 27 86 BF
15 BE 40 6F
"""

reference_swatches = """
0       00      00      00
1       FF      00      00
2       00      FF      00
3       00      00      FF
4       7F      7F      7F
5       FF      FF      00
6       00      FF      FF
7       FF      00      FF
8       40      40      40
9       FF      00      00
10      00      FF      00
11      00      00      FF
12      C0      C0      C0
13      FF      FF      00
14      00      FF      FF
15      FF      00      FF
"""

def swatch2srgb(swatches):
    srgb = []
    for l in swatches.splitlines():
        sl = l.split()
        if len(sl) < 4:
            continue
        r = int(sl[1],16)/255.
        g = int(sl[2],16)/255.
        b = int(sl[3],16)/255.
        srgb.append([r,g,b])
    return np.array(srgb)

uCAM = swatch2srgb(uCAM_swatches)
phone = swatch2srgb(phone_swatches)
reference = swatch2srgb(reference_swatches)