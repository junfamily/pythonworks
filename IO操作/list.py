# -*- coding: cp936 -*-
import os

#for root, dirs, files in os.walk('d:/Temp'):
    
   # for name in files:
   #     print name
for root, dirs, files in os.walk('E:\视频录像\Android深入浅出'):
    i = 1
    for name in files:
        print ( name )
        i = i + 1
