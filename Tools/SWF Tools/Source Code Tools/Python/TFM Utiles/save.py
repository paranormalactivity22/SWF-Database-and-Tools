import os, time, zlib, urllib, traceback, sys
from Tkinter import Tk; from tkFileDialog import askopenfilename, asksaveasfile

print("[-] TFMUtil: Create file...")
try:
    os.mkdir("langues")
except Exception as Error:
    print("[-] TFMUtil: "+str(Error))
time.sleep(1.0)
print("[-] TFMUtil: Download Langues...")
langue = urllib.URLopener()
for download in ["23", "24"]: #"1", "2", "3", "4", "5", "6", "7", "8", "fi", "fr", "he", "hr", "hu", "id", "it", "jp", "lt", "lv", "nl", "ph", "pl", "ro", "ru", "sk", "tr", "vk"]:
    langue.retrieve("http://transformice.com/langues/x_"+str(download)+".jpg", "./langues/"+str(download))
    print("[-] Download langue: ["+str(download.upper())+"]")
