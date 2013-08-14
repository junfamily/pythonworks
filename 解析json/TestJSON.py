# -*- coding: utf-8 -*-
import json
import urllib2

# 模拟IE7访问网站
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
urllib2.install_opener(opener)

f= urllib2.urlopen('http://www.weather.com.cn/data/sk/101010100.html')
jsontxt = f.read()
obj = json.loads(jsontxt)
print obj.keys()
print obj['weatherinfo']['city']


