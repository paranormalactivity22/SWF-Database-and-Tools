import os, time, zlib, urllib, traceback, sys
from Tkinter import Tk; from tkFileDialog import askopenfilename, asksaveasfile


print("[-] TFMUtil: Download Langues...")
langue = urllib.URLopener()
for download in ["ar", "bg", "br", "cn", "cz", "de", "en", "es", "fi", "fr", "he", "hr", "hu", "id", "it", "jp", "lt", "lv", "nl", "ph", "pl", "ro", "ru", "sk", "tr", "vk"]:
    os.system("md langues")
    langue.retrieve("https://www.transformice.com/langues/tfz_"+str(download), "./langues/tfz_"+str(download))
    print("[-] Download langue: ["+str(download.upper())+"]")
print("Created by Sim_pro")