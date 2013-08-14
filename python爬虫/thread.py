# -*- coding: utf-8 -*-
import Queue
import threading
import urllib2
import re
import time

queue = Queue.Queue()

class threadUrl(threading.Thread):
    '''建立线程来获取网页中需要的'''
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
               
    def run(self):
        while True:
            url = self.queue.get()
            try:
                f = urllib2.urlopen(url)
                print '打开网页:'+url[-30]+'成功\n'
            except urllib2.URLError, e:
                if hasattr(e, 'reason'):
                    print '打开失败的原因:', e.reason
                elif hasattr(e, 'code'):
                    print '打开失败的代码:', e.code
                else:
                    print '打开失败:', e

            else:
                html = f.read()

                begin=html.find('<ul class="deals-list">')
                end=html[begin:].find('</ul>')
                chunk=html[begin:begin+end]

                # 生成正则表达式匹配条件
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

                self.queue.task_done()

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
                #print(data)
        except:
            print 'url解析错误'

start = time.time()
def main():
    # httpHandler = urllib2.HTTPHandler(debuglevel=1)
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
    urllib2.install_opener(opener)

    
    # 生成线程池
    for i in range(5):
        t = threadUrl(queue)
        t.setDaemon(True)
        t.start()
        
    for i in range(1, 6):
        url = 'http://tuan.inlishui.com/team/inaadex.php?page=' + str(i)
        queue.put(url)

    # 等待全部完成后
    queue.join()

main()
print '完成所需时间：%s' % (time.time() - start)
