#-*- coding:utf-8 -*-

import httplib ,re ,urllib2 ,socket

Accept = "image/gif ,image/x-xbitmap ,image/jepg ,image/pjpeg .*/*"
AcceptLanguage = "zh-cn"
UserAgent = "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0 )"


def get(url,date=None,headers=None,referer=None):
    request = urllib2.Request(url)
    if date:
            request.add_data(data)
    if headers:
            for key in headers.keys():
                    request.add_header(key,headers[key])
    if not request.has_header("User-Agent"):
            request.add_header("User-Agent",UserAgent)
    if not request.has_header("Referer"):
            request.add_header("Referer",referer)
    if not request.has_header("Accept"):
            request.add_header("Accept",Accept)
    if not request.has_header("Accept-Language"):
            request.add_header("Accept-Language",AcceptLanguage)
    if None and not request.has_header("Accept-Encoding"):
            request.add_header("Accept-Encoding",AcceptELanguagencoding)



    method = request.get_method()
    try:
        result = urllib2.urlopen(request)
        return result
    except urllib2.URLError,error:
        pass
    except socket.error,error:
        pass
    except:
        pass
    return  None



