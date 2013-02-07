# coding=gbk

import requests
import re
#print requests.__doc__
import sys
import codecs,urllib,urllib2
import smtplib
import email.mime.text
import sqlite3
import shelve
f = open('text.txt','wb')

def Mail(username,password,mail_from,mail_to,subject,content):
    HOST = 'smtp.gmail.com'  
    PORT = 25
    smtp = smtplib.SMTP()
    smtp.set_debuglevel(1)
    try:  
        print smtp.connect(HOST,PORT)
        smtp.starttls()
        smtp.login(username,password)  
        msg = email.mime.text.MIMEText(content, 'html', 'gbk')  
        msg['From'] = mail_from
        msg['To'] = ';'.join(mail_to)
        msg['Subject']= subject
        smtp.sendmail(mail_from,mail_to,msg.as_string())  
        smtp.quit()  

    except Exception,e:  
        print e
        return -1
g_html_head="""
<html xmlns="http://www.w3.org/1999/xhtml">

<head>

<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />

<meta http-equiv="X-UA-Compatible" content="IE=8" />

<meta content="FFDY" name="keywords" />

<title>�ŷŵ�Ӱ ���µ�Ӱ ���߹ۿ�</title>

<link href="css.css" rel="stylesheet" type="text/css" />

<script type="text/javascript" src="function-1.0.1.js"></script>

</head>

<body>

<div class="container">

  <div class="col1">

    <h2>���µ�Ӱ���أ�</h2>

    <div class="content">

      <ul>

"""
g_html_tail="""
        
        
      </ul>

    </div>

  </div>

</div>

</body>

</html>

"""
g_html_content = """
<li><a href="%s" target="_blank">%s</a>
"""



def main():
    global g_html_content
    global g_html_tail
    global g_html_head
    g_count = 0
    save = shelve.open('urls.dat')
    fout = open('test.html','wb')
    while g_count<5:
        g_count+=1
        try:
            url = 'http://www.ffdy.cc/'
            #opener = urllib2.urlopen(url)
            #urllib2.install_opener(opener)
            print 'start open : %s' % url
            req = urllib2.Request(url)
            print 'reading ...'
            c = urllib2.urlopen(req).read()
            print c
            new_list = re.findall('\<a href\="(movie.*?)" target\=\"_blank\"\>([^\<].*?)\</a\>',c)
            content = g_html_head
            new_count = 0
            for item in new_list:
                url = 'http://www.ffdy.cc/'+item[0]
                if save.has_key(url):
                    print 'Repeat : %s' % save[url]
                    continue
                save[url]=item[1]
                content+= g_html_content % (url,item[1])
                print item[0],item[1]
                new_count+=1
            content+= g_html_tail
            fout.write(content)
            #print ';'.join(['80424704@qq.com'])
            if new_count>0:
                print 'New : %d' % new_count
                Mail('harkyes@gmail.com','harktest','harkyes@gmail.com',['80424704@qq.com'],'FFDY.cc',content)
            else:
                print 'There is No New Vedio'
        except Exception,e:
            print 'FAIL :',e
            print 'TRY Again'
        else:
            print 'Fetch OK'
            break
if __name__ == '__main__':
    main()
