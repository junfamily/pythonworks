# -*- coding: cp936 -*-
# for bbs.pcbeta.com
import cookielib,urllib2,urllib
import time
import re, random


msg = ['多谢楼主','Mark',
        '正在找这个，谢谢',
        '谢谢分享',
       '虽然我不需要, 但感觉楼主是好人.',
       '支持一下']

httpHandler = urllib2.HTTPHandler(debuglevel=1)
cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),httpHandler)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'),
                     ('Accept-Encoding', 'gzip,deflate')]

urllib2.install_opener(opener)



def login():
    usr = 'sendoh'
    pwd = '2747885612'
    web= 'http://bbs.inlishui.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'

    postdata =urllib.urlencode({'username':usr, 'password':pwd,'quickforward':'yes', 'handlekey':'ls'})

    req = urllib2.urlopen(web,postdata)
    print '...login succeed!'

def farm():
    '''这个就是灌水函数了'''
    # 疯狂灌水区
    url ='http://bbs.inlishui.com/forum-21-1.html'
    
    res = urllib2.urlopen(url).read()

    formhash = re.compile(r'member.php\?mod=logging&amp;action=logout&amp;formhash=(.*?)"').findall(res)[0]
    print formhash

    # 已进行到67页
    for i in range(1, 10001):
        url= 'http://bbs.inlishui.com/forum-21-%s.html' % i
        res = urllib2.urlopen(url).read()
        print url
        tids = re.compile(r'bbs.inlishui.com/thread-(.*?)-.*.html" onclick').findall(res)
    
        for tid in tids:
            # http://bbs.inlishui.com/thread-549996-1-1.html
            url = 'http://bbs.inlishui.com/forum.php?mod=post&infloat=yes\
&action=reply&fid=21&extra=&tid=%s&replysubmit=yes&inajax=1' % str(tid)
            print url
            postData = {
                'formhash':str(formhash),
                'handlekey':'reply',
                'noticeauthor':'',
                'noticetrimstr':'',
                'noticeauthormsg':'',
                'usesig':'0',
                'subject':'',
                'message':random.choice(msg),
                'replysubmit':'true'
            }
            postData = urllib.urlencode(postData)
            req = urllib2.Request(url = url, data = postData )
            kk = urllib2.urlopen(req).read()
            # 随机等待一会再发贴
            time.sleep(random.randint(1,10))
        print '第%s页已完成' % i

def test():
    for i in range(1, 3):
        url= 'http://bbs.inlishui.com/forum-21-%s.html' % i
        res = urllib2.urlopen(url).read()

        tids = re.compile(r'bbs.inlishui.com/thread-(.*?)-.*.html" onclick').findall(res)
        print tids
if __name__=='__main__':
    login()
    farm()

