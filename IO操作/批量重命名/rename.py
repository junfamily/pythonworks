# -*- coding: utf-8 -*-
import os

# first 
PERFIX = 'img'
# number 
LENGTH = 2
# star with base
BASE = 1
# only rename file have format
FORMAT = 'jpg'
# where to rename
PATH = 'D:\\Wallpaper'


def padleft(str, num, padstr):
    # add zero if have two length
    stringlength = len(str)
    n = num - stringlength
    if n >=0:
        str = padstr*n+str
    return str

def rename():
    print 'the files in %s will be renamed' %PATH
    input = raw_input('press y to continue\n')
    if input !='y':
        exit()

    i = BASE - 1
    file_names = os.listdir(PATH)
    for fn in file_names:
        i = i + 1
        if os.path.isfile(os.path.join(PATH,fn)):
            mubmer = str(i)
            name = padleft(mubmer, LENGTH, '0')
            t = fn.split('.')
            newname = PERFIX + name + '.'+t[-1]

            if FORMAT == '':
                os.rename(os.path.join(PATH,fn),os.path.join(PATH,newname))
            else:
                if t[-1] == FORMAT:
                    os.rename(os.path.join(PATH,fn),os.path.join(PATH,newname))
                else:
                    i = i - 1
        else:
            i = i - 1
    print 'done.'

if __name__=='__main__':
    rename()
