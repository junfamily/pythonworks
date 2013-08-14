# -*- coding: utf-8 -*-

import time


start = time.time()
def main():
    f = open('data.txt','a+')
    f.write('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    for i in range(10):
        f.write('bbbbbbbbbbbbbbbbbbbbbb'+str(i)+'\n' )
    f.write('ccccccccccccccccccccccccccccccc')
    f.close()
    print '完成所需时间：%s' % (time.time() - start)

if __name__ == '__main__':
    main()

