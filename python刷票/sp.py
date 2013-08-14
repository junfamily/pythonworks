# -*- coding: cp936 -*-
import urllib2,time
import urllib

# 模拟IE7访问网站
httpHandler = urllib2.HTTPHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler)
opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
urllib2.install_opener(opener)

# 获取该网页的数据
def get():
    url = 'http://wwv.zhxww.net/rkb/applychankan.aspx?id=185'
    data = '__VIEWSTATE=%2FwEPDwULLTE4MTU0MzIzMTUPZBYCAgEPZBYUZg8WAh4E\
VGV4dAWeASAgPGEgaHJlZj0iamF2YXNjcmlwdDpjaGFuZ2VfaW1nKCd1cGxvYWQvaW1hZ2U\
vMTIwOTExMDQwNTIxMDMxMi5qcGcnKSI%2BPGltZyBzcmM9InVwbG9hZC9pbWFnZS9zbDEy\
MDkxMTA0MDUyMTAzMTIuanBnIiB3aWR0aD0iMTMwIiBoZWlnaHQ9IjEwNSIgYm9yZGVyPSI\
wIj48L2E%2BZAIBDxYCHwAFngEgIDxhIGhyZWY9ImphdmFzY3JpcHQ6Y2hhbmdlX2ltZygn\
dXBsb2FkL2ltYWdlLzEyMDkxMTA0MDUyMTA3ODEuanBnJykiPjxpbWcgc3JjPSJ1cGxvYWQ\
vaW1hZ2Uvc2wxMjA5MTEwNDA1MjEwNzgxLmpwZyIgd2lkdGg9IjEzMCIgaGVpZ2h0PSIxMD\
UiIGJvcmRlcj0iMCI%2BPC9hPmQCAg8WAh8ABZ4BICA8YSBocmVmPSJqYXZhc2NyaXB0OmNo\
YW5nZV9pbWcoJ3VwbG9hZC9pbWFnZS8xMjA5MTEwNDA1MjExMDkzLmpwZycpIj48aW1nIHNy\
Yz0idXBsb2FkL2ltYWdlL3NsMTIwOTExMDQwNTIxMTA5My5qcGciIHdpZHRoPSIxMzAiIGh\
laWdodD0iMTA1IiBib3JkZXI9IjAiPjwvYT5kAgMPFgIfAAUP5bm456aP5oiR5Lus5LuoZA\
IEDxYCHwBlZAIFDxYCHwBlZAIGDxYCHwAFCzEzNzM4ODMwOTY5ZAIHDxYCHwAFDOa4r%2BW\
fjuiKseWbrWQCCA8WAh8ABdwF44CA44CAMDDlubTvvIzmiJHku6zlnKjmoKHlm63nm7jpgY\
fvvIw8YnIgLz7jgIDjgIAwMuW5tO%2B8jOS9oOi3n%2BaIkeihqOeZvSDvvIw8YnIgLz7jg\
IDjgIDnhLblkI7lvIDlp4vmiJHku6znmoTnlJzonJzniLHmg4XvvJs8YnIgLz48YnIgLz7j\
gIDjgIAwNOW5tO%2B8jOaIkeavleS4muadpeWIsOmVh%2Ba1t%2B%2B8jDxiciAvPuOAgOOA\
gOS9oOeVmeWcqOS6huadreW3nu%2B8jDxiciAvPuOAgOOAgOmCo%2BaXtuWAmeeahOW5uOem\
j%2BaYr%2Bavj%2BWkqea4heaZqOWPq%2BaIkei1t%2BW6iueahOa4heiEhueUteivne%2B\
8jDxiciAvPuOAgOOAgOaYr%2BS5mOeBq%2Bi9puadpeeci%2BS9oOeahOeDreWIh%2BW%2F\
g%2BaDhe%2B8mzxiciAvPjxiciAvPuOAgOOAgDA35bm077yM5oiR5Lus57uT5ama77yMPGJ\
yIC8%2B44CA44CA5Y%2Bv5piv6L%2BY5piv5Lik5Zyw5YiG5bGF77yMIDxiciAvPuOAgOOA\
gOmCo%2BaXtuWAmeeahOW5uOemj%2BaYr%2Ba3sea3seeahOaAneW%2Fte%2B8mzxiciAvP\
jxiciAvPuOAgOOAgDA45bm077yM5L2g5p2l5Yiw6ZWH5rW377yMPGJyIC8%2B44CA44CA6Y\
Kj5pe25YCZ5Zyo5LiA6LW35bCx5piv5bm456aP77ybPGJyIC8%2BPGJyIC8%2B44CA44CA5a\
aC5LuK77yM5oiR5Lus5omL54m15omL55yL552A5oiR5Lus55qE5a6d6LSd5Zu05Zyo5oiR5L\
us6Lqr6L655qyi5b%2Br5Lmx56qc77yMPGJyIC8%2B44CA44CA6L%2BZ5bCx5piv5bm456aP4\
4CCPGJyIC8%2B44CA44CA5oOz5ZKM5L2g5bCx6L%2BZ5qC35oWi5oWi5Y%2BY6ICB77yBPGJy\
IC8%2BZAIJDw8WAh4HVmlzaWJsZWdkZGSJHhI%2FT4Tx6QiRuHjeTdifLc%2Bz2g%3D%3D\
&Button2=%CD\
&__EVENTVALIDATION=%2FwEWAgLwkKH%2FDwK7q7GGCLQ%2Fhtt0DNgOdNWmAyiXk2d5Rg4M'
    try:
        req = urllib2.Request(url ,data)
   
        f = urllib2.urlopen(req)

        print('投票成功\n' )
    except:
        print('打开错误\n')

def code():
    #help(urllib)
    data = urllib.urlencode({'Button2':'投票'})
    print data
# 投票
def helloBtn():
    for i in range(1,2):
        get()
        time.sleep(1)
    print('投了10票\n')
helloBtn()
#code()
