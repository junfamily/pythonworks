# -*- coding: utf-8 -*-
import urllib2
import re

# 模拟IE7访问网站
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
urllib2.install_opener(opener)

def save(txt,name = 'data'):
    f = open('tmp/'+name+'.txt', 'a')
    f.write(txt)
    f.close()

def get(url):
    response = urllib2.urlopen(url)
    html = response.read()
    response.close()
    list1 = re.findall(r'<b>(\d+)<\\/b>',html)
    list2 = re.findall(r'<\\/b>(\d+)<\\/strong>',html)

    for i in range(len(list1)):
        data = list1[i] +'\t'+ list2[i]
        print data
        save(data, 'bbb')
        

for i in range(1,2):
    url = 'http://haoma.qq.com/static/asset/asset_index_%s.js' % i
    get(url)








