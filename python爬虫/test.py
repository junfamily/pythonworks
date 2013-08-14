# -*- coding: utf-8 -*-
import urllib2,urllib

httpHandler = urllib2.HTTPHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler)
opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'),
                     ('Accept-Encoding', 'gzip,deflate')]
urllib2.install_opener(opener)

site='','http://www.baidu.com','http://www.qq.com'
page = urllib2.urlopen(site[1]).read(1024)

print page

