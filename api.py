# coding=utf-8
import urllib
import draw
import pynput
import urllib2
import json
import random
import string
import time

def getImg(url):
    filename =  "images/%s"%(''.join(random.sample(string.ascii_letters + string.digits, 16)))
    f = urllib2.urlopen(url) 
    data = f.read() 
    with open(filename, "wb") as code: 
        code.write(data)
    return filename

def drawKey(key):
    #key = str(key)
    api = 'http://image.so.com/j?q=%s&src=srp&correct=&sn=1&pn='%key
    print api
    req = urllib2.urlopen(api)
    print req
    res = req.read()
    print res
    res = json.loads(res)
    res = res['list'][0]['thumb']
    filename = getImg(res)
#    time.sleep(3)
    if filename:
        i = draw.ImageDrawer(480,280)
        i.drawImage(filename)

    
if __name__ == '__main__':
    drawKey('蒙娜丽莎')