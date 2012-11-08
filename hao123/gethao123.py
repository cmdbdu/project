#-*- coding:utf-8 -*-

import os
import re
import sys
import urllib2
import threading
import time
def geturl(url,ttt):
    Tag=[]
    print url
    try:
        readurl=urllib2.urlopen(url).read()
        print "打开url成功"
    except:
        print "打开url失败"
        main(ttt,[url])
    #readurl=read.decode('utf-8')
    atag=re.findall(r'<a.*?</a>',readurl) 
    jsurl = re.findall('http://.*?[.]js',readurl)
    ##获取js文件
    for i in jsurl:
        try:
            getjs=urllib2.urlopen(i).read()
            print "打开url成功"
            time.sleep(1)
            bb = file(i.split('/')[-1],'w')
            print "创建js文件成功"
            bb.write(getjs)
            bb.close()
            print "获取",i.split('/')[-1],"文件成功"
        except:
            print "获取",i.split('/')[-1],"文件失败"
            pass

    ##获取css文件
    cssurl = re.findall('http://.*?[.]css',readurl)
    for i in cssurl:
        try:
            getjs=urllib2.urlopen(i).read()
            print "打开url成功"
            time.sleep(1)
            bb = file(i.split('/')[-1],'w')
            print "创建csss文件成功"
            bb.write(getjs)
            bb.close()
            print "获取",i.split('/')[-1],"文件成功"
        except:
            print "获取",i.split('/')[-1],"文件失败"
            pass

    ##获取xxx.hao123.com    <a>标签
    print "\t","\t","\t"
    print "获取xxx.hao123.com    <a>标签"
    for i in atag:
        bbb = re.findall(r'<a.*?hao123.com.*?>.*?</a>',i)
        if bbb==[]:
            pass
        else:
            #截取 url
            hrefs=re.findall(r'http:.*?[\'"]',bbb[0])[0]
            href=hrefs.split(hrefs[-1])[0]
            print href
            Tag.append(href)
    ##获取xxx.hao123.com    <img>标签
    print "\t","\t","\t"
    print "获取xxx.hao123.com    <img>标签"
    imgtags=re.findall(r'<img.*?>',readurl) 
    for ima in imgtags:
        #ccc = re.findall('<img.*?</img>',ima)
        print "获取xxx.hao123.com    <img>标签"
        #print ccc
        print ima
        time.sleep(2)


    Tags=list(set(Tag))
    print "去重以后共获取有效url",len(Tag),"个"
    for url in Tags:
        ttt+=1
        main(ttt,Tags)

def main(tt,Tags):
    if tt <= sys.argv[2] :
        print '第',tt,'次爬虫'
        if len(Tags)>0:
            for url in Tags:
                S = threading.Thread(geturl(url,tt))
                S.start()
        else:
            print '没有有效的url'
    else:
        print '时间到'
        sys.exit()




if __name__=='__main__':
    print '爬虫开始'
    t = 1
    Tags=[ sys.argv[1]]
    time.sleep(1)
    main(t,Tags) 
