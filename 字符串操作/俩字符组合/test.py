# -*- coding: utf-8 -*-

def savefile(txt):
    f = file('1.txt', 'a')
    f.write(txt)
    f.close()

sm = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l',
      'g', 'k', 'h', 'j', 'q', 'x', 'zh','ch',
      'sh','r', 'z', 'c', 's']
ym = ['a', 'o', 'e', 'ai', 'ei', 'ao', 'ou', 'an',
      'en','ang','eng','ong','i','ia', 'ie', 'iao','aou',
      'ian','in','iang','ing','iong','u','ua','uo',
      'uai','uei','uan','uen','uang','ueng','ue','uan','un']

def main():
    num = 0
    for x in sm:
        for y in ym:
            txt =  x + y+'\n\r'
            num = num + 1
            #savefile(txt)
    print 'done. the munber is',num

if __name__ == '__main__':
    main()
