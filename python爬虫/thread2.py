# -*- coding: utf-8 -*-
import Queue
import threading
import urllib2
import re
import time

queue = Queue.Queue()
out_queue = Queue.Queue()

class threadUrl(threading.Thread):
    '''    获取内容       '''
    def __init__(self, queue, out_queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while True:
            url = self.queue.get()
            
            response = urllib2.urlopen(url)
            html = response.read()
            begin=html.find('<ul class="deals-list">')
            end=html[begin:].find('</ul>')
            chunk=html[begin:begin+end]

            self.out_queue.put(chunk)
            self.queue.task_done()

class datamineThread(threading.Thread):
    ''' 数据挖掘  '''
    def __init__(self,out_queue):
        threading.Thread.__init__(self)
        self.out_queue = out_queue

    def run(self):
        while True:
            chunk = self.out_queue.get()

            reDate = re.compile(r'<p class="time">(.*)</p>')
            reTitle = re.compile(r'<h4><a href=".*" title="(.*)" target="_blank">')
            reNum = re.compile(r'<strong class="count">(\d+)</strong>')
            reYJ = re.compile(r'原价：<strong class="old"><span class="money">¥</span>(.*)</strong><br />折扣：')
            reZK = re.compile(r'折扣：<strong class="discount">(.*)折')
            reXJ = re.compile(r'现价：<strong><span class="money">¥</span>(.*)</strong><br />节省')
            reJS = re.compile(r'节省：<strong><span class="money">¥</span>(.*)</strong><br /></p>')

            myDate = reDate.findall(chunk)
            myTitle = reTitle.findall(chunk)
            myNum = reNum.findall(chunk)
            myYJ = reYJ.findall(chunk)
            myZK = reZK.findall(chunk)
            myXJ = reXJ.findall(chunk)
            myJS = reJS.findall(chunk)

            show(myDate, myTitle, myNum, myYJ, myZK, myXJ, myJS)

            self.out_queue.task_done()

def saveTxt(txt,name = 'data'):
    f = open(name+'.txt', 'a')
    f.write(txt)
    f.close

def show(a, b, c, d, e, f, g):
    if a:
        try:
            for x in range(len(a)):
                data = str(x) + '\t' + a[x] + '\t' + b[x] + '\t' + c[x] + '\t' + d[x] + '\t' + e[x] + '\t' + f[x] + '\t' + g[x] +'\n'
                #saveTxt(data)
        except:
            print 'url解析错误'

start = time.time()
def main():
    # httpHandler = urllib2.HTTPHandler(debuglevel=1)
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
    urllib2.install_opener(opener)



    for i in range(5):
        t = threadUrl(queue, out_queue)
        t.setDaemon(True)
        t.start()

    for i in range(1, 6):
        url = 'http://tuan.inlishui.com/team/index.php?page=' + str(i)
        queue.put(url)

    for i in range(5):
        dt = datamineThread(out_queue)
        dt.setDaemon(True)
        dt.start()

    queue.join()
    out_queue.join()

main()
print '完成所需时间：%s' % (time.time() - start)






