# coding=utf-8

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

    api = 'http://image.so.com/j?q=%s&src=srp&correct=&sn=1&pn='%key
    
    try:
        req = urllib2.urlopen(api)
        res = req.read()
        res = json.loads(res)
        res = res['list'][0]['thumb']
    except:
        return False
    filename = getImg(res)
#    time.sleep(3)
    if filename:
        i = draw.ImageDrawer(420,280)
        i.drawImage(filename)

    
if __name__ == '__main__':
    drawKey('企鹅')