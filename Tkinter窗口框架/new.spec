# -*- mode: python -*-
a = Analysis(['new.py'],
             pathex=['E:\\\xce\xc4\xb5\xb5\xd7\xca\xc1\xcf\\\xb8\xf6\xc8\xcb\xd7\xca\xc1\xcf\\Python\\Demo\\Tkinter\xb4\xb0\xbf\xda\xbf\xf2\xbc\xdc'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\new', 'new.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'new'))
