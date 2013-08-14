# -*- coding: utf-8 -*-
import ttk
import Tkinter
import time,os

class Config(Tkinter.Toplevel):
    def __init__(self, parent):
        Tkinter.Toplevel.__init__(self, parent)
        self.parent = parent
        self.configure(borderwidth=5)
        self.geometry("200x200+%d+%d" % (parent.winfo_rootx()+30,
                                  parent.winfo_rooty()+30))
        self.entry = Tkinter.Entry(self)
        self.entry.pack()
        button = ttk.Button(self, text="确定",command=self.ok)
        button.pack()
        self.wait_window()

    def ok(self):
        self.input = self.entry.get()
        self.destroy()

class App(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.configure(borderwidth=5)
        self.title('第五天堂制造')
        self.geometry('400x300')

        self.img_run=Tkinter.PhotoImage(file="icon/run.gif")
        self.img_config=Tkinter.PhotoImage(file="icon/config.gif")
        self.img_pause=Tkinter.PhotoImage(file="icon/pause.gif")
        self.img_log=Tkinter.PhotoImage(file="icon/log.gif")

        frame =Tkinter.Frame(self,height=30)
        frame.pack(fill=Tkinter.BOTH,pady=5)
        # run
        btn_run = ttk.Button(frame,image=self.img_run, command=self.run)
        btn_run.pack(side=Tkinter.LEFT)
        # config
        btn_conf = ttk.Button(frame,image=self.img_config,command=self.Config)
        btn_conf.pack(side=Tkinter.LEFT,padx=5)

        # log
        btn_log = ttk.Button(frame,image=self.img_log)
        btn_log.pack(side=Tkinter.LEFT)
        # 
        self.t = Tkinter.Text(self,relief=Tkinter.GROOVE)
        s = ttk.Scrollbar(self.t,command=self.t.yview) 
        s.pack(side=Tkinter.RIGHT,fill=Tkinter.Y)


        self.t.pack(fill=Tkinter.BOTH,expand=Tkinter.TRUE)
        self.t['state'] = 'disabled'
        self.t.config(yscrollcommand=s.set)
            
    def Config(self):
        d=Config(self)

    def run(self):
        
        self.t['state'] = 'normal'
        log = time.strftime('%X', time.localtime(time.time()))
        self.t.insert(Tkinter.END, log+'\n')
        self.t['state'] = 'disabled'





app =App()
app.mainloop()
