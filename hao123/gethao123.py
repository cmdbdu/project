#-*- coding:utf-8 -*-

import os
import re
import sys
import urllib2
import threading
import time

def geturl(url,times):
    readurl=urllib2.urlopen(url).read()
    #readurl=read.decode('utf-8')
    atag=re.findall(r'<a.*hao123[.]com.*?>.*?</a>',readurl) 
    imgtag=re.findall(r'<img.*?>.*?</img>',readurl) 
    aa = file('aaa.txt','w')
    print len(atag)
    x=0
    for i in atag:
        bbb = re.findall(r'<a.*?hao123[.]com.*?>.*?</a>',i)
        print bbb
        print x
        x+=1
        time.sleep(0.5)
        #for j in bbb:
        #    aa.write(j)
    for ima in imgtag:
        ccc = re.findall('<img.*?</img>',ima)
        print ccc
        time.sleep(2)
        for l in ccc:
            aa.write(l)
    aa.close()

if __name__=='__main__':
        geturl(sys.argv[1],sys.argv[2]) 
