# -*- coding: utf-8 -*-
import urllib2
import re
import time

# 模拟IE7访问网站
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
urllib2.install_opener(opener)

def save(txt,name = 'data1'):
    f = open('tmp/'+name+'.txt', 'a')
    f.write(txt)
    f.close

def get(url):
    try:
        response = urllib2.urlopen(url)
        print '打开网址' + url + '        OK!' + '   用时：%s秒' % (time.time()-start)
    except:
        print '打开错误' + url
    print '-----------------------'
    html = response.read()
    response.close()
    begin=html.find('<ul class="deals-list">')
    end=html[begin:].find('</ul>')
    str1=html[begin:begin+end]
    try:
        date = re.findall(r'<p class="time">(.*?)</p>',str1)
        title = re.findall(r'<h4><a href=".*" title="(.*?)" target="_blank">',str1)
        num = re.findall(r'<strong class="count">(\d+)</strong>',str1)
        YJ = re.findall(r'原价：<strong class="old"><span class="money">¥</span>(.*?)</strong><br />折扣：',str1)
        ZK = re.findall(r'折扣：<strong class="discount">(.*?)折',str1)
        XJ = re.findall(r'现价：<strong><span class="money">¥</span>(.*?)</strong><br />节省',str1)
        JS = re.findall(r'节省：<strong><span class="money">¥</span>(.*?)</strong><br /></p>',str1)
    except:
        print '解析错误'

    for i in range(len(title)):
        data = str(i) + '\t' + date[i] + '\t' + title[i] + '\t' + num[i] + '\t' + YJ[i] + '\t' + ZK[i] + '\t' + XJ[i] + '\t' + JS[i] +'\n'
        print data
        save(data,'aaa')
    print '-----------------------'
        
start = time.time()
def main():
    for i in range(1, 2):
        url = 'http://tuan.inlishui.com/team/index.php?page=%s' % i
        get(url)

main()
print '完成所需时间：%s' % (time.time() - start)






