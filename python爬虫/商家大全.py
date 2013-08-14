# -*- coding: utf-8 -*-
#import urllib
import urllib2
import re
import time
#from BeautifulSoup import BeautifulSoup

# 模拟IE7访问网站
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
urllib2.install_opener(opener)

# 获取该网页的数据
start = time.time()
def get(url):
    try:
        page = urllib2.urlopen(url)
        print page.headers.getparam('charset')
        print '打开网址' + url + '        OK!' + '   用时：%s秒' % (time.time()-start)
    except:
        print '打开错误' + url
    print '-----------------------'
    html = page.read()
    '''
    f = open('tmp/tmp.html', 'w')
    f.write(html)
    f.close()
    print '保存完毕     用时：%s秒' % (time.time() - start)
    '''
    #fp = open('tmp/tmp.html')
    #html = fp.read()
    # 用BeautifulSoup 分析页面代码
    #soup = BeautifulSoup(html)
    # for i in range(2):
    try:
        name = re.findall(r'<a href="/ls634/" title="(.*?)" ', html)
        addr = re.findall(r'</strong>(.*?)&nbsp;&nbsp;<a href="/item-bigmap',html)
        tel = re.findall(r'<span class="shangjia_hueifu"><strong>(.*?)</strong>',html)
    except:
        name = "UNKNOWN"

    #print cname
    for i in range(len(name)):
        data = name[i]+'\t'+tel[i]+'\t'+addr[i]
        # = addr[i]
        print data
        f = open('tmp/data.txt', 'a')
        f.write(data+'\n')
        f.close()
        #print '保存完毕     用时：%s秒' % (time.time() - start)
    print '-----------------------'



# 生成URL网址
# example:
# http://shangjia.inlishui.com/item-list-catid-88-aid-0-type-normal-num-20-total-368-page-1.html
# http://shangjia.inlishui.com/item-list-catid-88-aid-0-type-normal-num-20-total-368-page-2.html
# 一共有19页
for i in range(10,11):
    url = 'http://shangjia.inlishui.com/\
item-list-catid-88-aid-0-type-normal\
-num-20-total-368-page-%s.html' % i
    get(url)


print '执行完毕     用时：%s秒' % (time.time() - start)
