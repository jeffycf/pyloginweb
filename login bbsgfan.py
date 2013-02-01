
#import HTMLParser 
#import urlparse 
import urllib 
import urllib2 
import cookielib 
#import string 
#import re 
import md5
#import time


def login():
    hosturl='http://bbs.gfan.com'
    posturl='''http://bbs.gfan.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'''
    cj=cookielib.LWPCookieJar()
    cookie_support=urllib2.HTTPCookieProcessor(cj)
    opener=urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    h=urllib2.urlopen(hosturl)
    pwd=md5.new('********')
    pp=pwd.hexdigest()
    headers={'Host':'bbs.gfan.com','User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",}
    postData={'fastloginfield':'username','username':'******','password':pp,'quickforward':'yes','handlekey':'ls',
              'Referer':"http://bbs.gfan.com/forum.php"}
    postData=urllib.urlencode(postData)
    request=urllib2.Request(posturl,postData,headers)
    print request
    response=urllib2.urlopen(request)
    #text=response.read()
    dakaurl="http://bbs.gfan.com/home.php?mod=task&do=apply&id=43"
    #dakaurl="http://bbs.gfan.com/home.php?mod=task&do=view&id=43"
    daka=urllib2.urlopen(dakaurl)
    dd=daka.read()
    
    print dd
    fp=open('c:/test.html','a+')
    fp.write(dd)
    fp.close()


if __name__ == '__main__':
    login()
    
    #login()
    print "Login in bbs.gfan.com"
