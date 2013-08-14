# -*- coding: utf-8 -*-

from distutils.core import setup
import glob
import py2exe

#includes = ["encodings", "encodings.*"]
options = {"py2exe":  
            {   "compressed": 1,  #压缩
                "optimize": 2,  
               # "includes": includes,  
               # "bundle_files": 1  # 1 打包成一个exe
            }  
          } 

setup(
    version = "1.0.0",
    description = "this is findshded by James",
    name = "app",

    options = options,  
    zipfile=None,  
    
    windows = ["new.py"],
    data_files=[("icon",glob.glob('icon/*.gif'))],
    )
