# -*- coding:utf-8 -*-
import os
import re
import sys
from urllib2 import Request,urlopen,URLError,HTTPError
import urllib2
import threading
import time
import datetime


def geturl(url):
    Tag=[]
    print '开始获取网址为',url,'的数据'
    time.sleep(2)
    try:
        readurl=urllib2.urlopen(url).read()
        print "打开",url,"成功"
    except URLError,e:
        print "URLError",e
        sys.exit()
    except HTTPError,e:
        print "HTTPError",e
        sys.exit()
    except :
        print "打开url失败!!网络错误。请检查你的网络是否畅通，网络地址应该是‘http：//xxx.xxx’格式"
        time.sleep(2)
    #readurl=read.decode('utf-8')
    hisurl.append(url)
    atag=re.findall(r'<a.*?</a>',readurl) 
    jsurl = re.findall('http://.*?[.]js',readurl)
    ##获取js文件
    for i in jsurl:
        try:
            getjs=urllib2.urlopen(i).read()
            print "打开",i,"成功"
            time.sleep(1)
            bb = file(i.split('/')[-1],'w')
            print "创建js文件成功"
            bb.write(getjs)
            bb.close()
            print "获取",i.split('/')[-1],"文件成功"
        except URLError,e:
            print "获取",i.split('/')[-1],"文件失败"
            print "URLError",e
        except HTTPError,e:
            print "获取",i.split('/')[-1],"文件失败"
            print "HTTPError",e
        except:
            print "获取",i.split('/')[-1],"文件失败"
            pass

    ##获取css文件
    cssurl = re.findall('http://.*?[.]css',readurl)
    for i in cssurl:
        try:
            getjs=urllib2.urlopen(i).read()
            print "打开",i,"成功"
            time.sleep(1)
            bb = file(i.split('/')[-1],'w')
            print "创建css文件成功"
            bb.write(getjs)
            bb.close()
            print "获取",i.split('/')[-1],"文件成功"
        except URLError,e:
            print "获取",i.split('/')[-1],"文件失败"
            print "URLError",e
        except HTTPError,e:
            print "获取",i.split('/')[-1],"文件失败"
            print "HTTPError",e
        except:
            print "获取",i.split('/')[-1],"文件失败"
            pass

    ##获取xxx.hao123.com    <a>标签
    print "\n"
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
    print "获取xxx.hao123.com    <img>标签"
    imgtags=re.findall(r'<img.*?>',readurl) 
    for ima in imgtags:
        print ima

    Tags=list(set(Tag))
    newurl = list(set(hisurl)^set(Tags))
    for i in newurl:
        urls.append(i)

def thread():
    thrurl=urls[0:int(sys.argv[2])]
    print thrurl
    for i in thrurl:
        t = threading.Thread(target=geturl,args=(i,))
        threads.append(t)
    print threads
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
if __name__=='__main__':
    print '爬虫开始'
    starttime = datetime.datetime.now()
    threads = []
    urls = []
    hisurl = []
    geturl(sys.argv[1])
    time.sleep(5)
    thread()
    print '爬虫结束'
    endtime = datetime.datetime.now()
    print "程序运行时间是",(endtime-starttime).seconds,'秒,共获取了',len(hisurl),'个网站的数据'
