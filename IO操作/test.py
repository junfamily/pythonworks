# -*- coding: cp936 -*-
import os

cwd = os.listdir('E:\��Ƶ¼��\Android����ǳ��')
i = 1
for name in cwd:
    print i,name
    i=i+1
    if 1:
        t = name.split('.')
        m = len(t)
        print t[m-1]
