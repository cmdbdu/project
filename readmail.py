# !/usr/bin/env python
# coding:UTF-8
# Created Time:2014-12-25
# Auther dub

import email
import imaplib


class Connect:
    '''
    链接指定邮件，并读取未读邮件内容
    '''
    def __init__(self, username, password, server="imap.126.com", port=993):
        self.password = password
        self.username = username
        self.server   = server
        self.port     = port

    def connect(self):
        try:
            conn = imaplib.IMAP4_SSL(self.server, self.port)
            return conn
        except Exception, e:
            pass 
    
    def loginemail(self):
        try:
            conn = self.connect()
            conn.login(self.username, self.password)
        except Exception, e:
            pass

    def logoutemail(self):
        try:
            conn = self.connect()
            conn.logout()
        except Exception, e:
            pass

class Parse(Connect):
    def __init__(self,username,password,unread):
        Connect.__init__(self, username, password)
        self.unread = unread

    def start(self):
        conn = self.connect()
        conn.login(self.username, self.password)
        try:
           typ,unread_count = conn.select(self.unread)
           if typ == "OK":
               typ,msgmums = conn.search(None,"UNSEEN")
               for msg in msgmums[0].split():
                   typ,data = conn.fetch(msg,"(RFC822)")
                   for response_part in data:
                       if isinstance(response_part,tuple):
                           mail_part = email.message_from_string(response_part[1])
                           return mail_part
                   typ,response_part = unread_count.store(num,"+FLAGES",r"(\Seen)")
        except Exception, e:
            return "some error here!"

    def pare_content(self):
        mail = self.start()
        mail_info = {}
        try:
            From = mail['From'].split(' ')[1]
            To = mail['To'].split(' ')[1]
            sub = email.Header.decode_header(mail['Subject'])
            Subject = unicode(sub[0][0],sub[0][1])
            mail_info['From'] = From
            mail_info['To'] = To
            mail_info['Subject'] = Subject
            mail_info['Date'] = mail['Date']

        except Exception,e:
            return  'some error here!'

        try:
            for part in mail.walk():
                if not part.is_multipart():
                    name = part.get_filename()
                    contenttype = part.get_content_type()
                    if contenttype == 'text/plain':
                        #只取前两行内容
                        content = part.get_payload(decode=True).split('\n')[0:2]
                        mail_info['content'] = content

                    #读取附件
                    if name:
                        h = email.Header.Header(name)
                        dh = email.Header.decode_header(h)  
                        file_name = dh[0][0] 
                        file_code = dh[0][1] 
                        if not file_code:
                            file_code = 'utf8'
                        data = part.get_payload(decode=True)
                        mail_info['file_name'] = file_name
                        mail_info['data'] = data

            return mail_info

        except Exception, e:
            return "some  error about walk  here!"

