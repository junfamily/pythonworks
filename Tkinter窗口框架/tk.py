# -*- coding: utf-8 -*-
from Tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.showText = Text(self,width=60,height=15)
        self.showText.pack()

        self.btn_setting = Button(self, text = '设置', width=8, height=1, command = self.btnSetting)
        self.btn_setting.pack(side = 'right', padx=10)
        self.btn_stop = Button(self, text = '停止', width=8, height=1, command = self.btnStop)
        self.btn_stop.pack(side = 'right', padx=10)
        self.btn_start = Button(self, text = '开始', width=8, height=1, command = self.btnStart)
        self.btn_start.pack(side = 'right', padx=10, pady=10)   

    def btnStart(self):
        self.showText.insert(END, 'Server:\n')

    def btnSetting(self):
       win = App2(self)

    def btnStop(self):
        print self.showText


        



class App2(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, app)
        self.app =app
        self.createWidgets()

    def btnStart(self):
        print 'aaaaaaaaaaaaaaaaaaaaaaa'

    def btnSetting(self):
        lable_status.pack(side = 'right')

    def btnStop(self):
        lable_status.pack(side = 'bottom')

    def createWidgets(self):
        self.lable_status = Label(self, text="Hello, world!")
        self.lable_status.pack()

        self.btn_start = Button(self, text = '开始', width=8, height=2, command = self.btnStart)
        self.btn_start.pack(side = 'left', padx=10, pady=10)

        self.btn_setting = Button(self, text = '设置', width=16, height=2, command = self.btnSetting)
        self.btn_setting.pack(side = 'left', padx=10)

        self.btn_stop = Button(self, text = '停止', width=16, height=2, command = self.btnStop)
        self.btn_stop.pack(side = 'right', padx=10)


root = Tk()

app = App()
root.title('银河信息采集系统')
root.geometry('500x300')
root.mainloop()
