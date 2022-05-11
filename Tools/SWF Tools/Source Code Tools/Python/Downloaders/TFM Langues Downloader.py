# -*- coding: cp1252 -*-
import os
import urllib2
import time
from datetime import datetime
def getTime():
        TIME = str(datetime.now())[11:].split(":")
        TIME = TIME[0]+":"+TIME[1]+":"+TIME[2][:2]
        return str(TIME)
Start = datetime.now()
    
def getDateTime():
    time = str(datetime.now())    
    time = time.split(" "); time = str(time[1]); time = time.split("."); time = time[0].split(":")
    tmd = {}
    tmd['hour'] = time[0]
    if tmd:
        time = str(tmd['hour'])
        return time

print '*' * 80
print 'Program Created By: Waysdi [Robertito]'
print 'Credits: Gfdants [Base Program], ~Nuke [Help the source code] and Waysdi [Creator Oficial of the program]'
print '*' * 80

langues = ['ar', 'br', 'cn', 'de', 'en', 'es', 'fr', 'hu', 'id', 'nl', 'no', 'pl', 'ro', 'ru', 'tr', 'bg']
try:
     os.makedirs('langues')
except:
    pass

def main():
     for Namefile in langues:
          print "Um moment, Please Wait...."
          print "Okay System Ready"
          print "Downloading langues tfm_"+str(Namefile)
          url = urllib2.urlopen("http://www.transformice.com/langues/tfm_"+str(Namefile))
          data = url.read()
          folder = open("./langues/tfm_"+str(Namefile), "wb")
          folder.write(data)
          folder.close()
if __name__=="__main__":
        os.system('color B')
        os.system('title TFM Downloader Langues, Are '+str(getDateTime())+' hours')
        main()
