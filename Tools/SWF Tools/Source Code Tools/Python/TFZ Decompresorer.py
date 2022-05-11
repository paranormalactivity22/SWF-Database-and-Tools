import Tkinter
import os, glob, re, random, time, zlib, urllib
import tkMessageBox
os.system("title TFZ Decompresorer")
os.system("echo [-] TFZ Decompresorer By Lucas")
top = Tkinter.Tk()
top.title("TFZ Decompresorer")

canvas1 = Tkinter.Canvas(top, width = 350, height = 250) 
canvas1.pack()


def Download():
    print("[-] TFZ Decompresorer: Create file...")
    try:
        os.mkdir("langues")
    except Exception as Error:
        print("[-] TFZ Decompresorer: "+str(Error))
    time.sleep(1.0)
    print("[-] TFZ Decompresorer: Download Langues...")
    langue = urllib.URLopener()
    for download in ["ar", "bg", "br", "cn", "cz", "de", "en", "es", "fi", "fr", "he", "hr", "hu", "id", "it", "jp", "lt", "lv", "nl", "ph", "pl", "ro", "ru", "sk", "tr", "vk"]:
        langue.retrieve("http://transformice.com/langues/tfz_"+str(download), "./langues/tfz_"+str(download))
        print("[-] Download langue: ["+str(download.upper())+"]")
    print("[-] Finish\n")
    tkMessageBox.showinfo("TFZ Decompresorer", "Succesfully Downlaoded!")

def Decompress():
    print("[-] TFZ Decompresorer: Decompress Langues...")
    try:
        for use in ["ar", "bg", "br", "cn", "cz", "de", "en", "es", "fi", "fr", "he", "hr", "hu", "id", "it", "jp", "lt", "lv", "nl", "ph", "pl", "ro", "ru", "sk", "tr", "vk"]:
            langue = open("./langues/tfz_"+str(use), 'rb').read()
            decompress = zlib.decompress(langue)
            file = open("./langues/tfm_"+str(use), 'wb')
            file.write(decompress)
            file.close()
            print("[-] Langue Decompress: ["+str(use.upper())+"]")
    except Exception as Error:
        print("[-] "+str(Error))
    print("[-] Finish\n")
    tkMessageBox.showinfo("TFZ Decompresorer", "Succesfully Decompressed")
    
def Compress():
    print("[-] TFZ Decompresorer: Compress Langues...")
    try:
        for use in ["ar", "bg", "br", "cn", "cz", "de", "en", "es", "fi", "fr", "he", "hr", "hu", "id", "it", "jp", "lt", "lv", "nl", "ph", "pl", "ro", "ru", "sk", "tr", "vk"]:
            langue = open("./langues/tfm_"+str(use), 'rb').read()
            compress = zlib.compress(langue)
            file = open("./langues/tfz_"+str(use), 'wb')
            file.write(compress)
            file.close()
            print("Langue Compress: ["+str(use.upper())+"]")
    except Exception as Error:
        print("[-] "+str(Error))
    print("[-] Finish\n")
    tkMessageBox.showinfo("TFZ Decompresorer", "Succesfully Compressed")

def About():
    tkMessageBox.showinfo("About", "Created by Lucas Aulamice.org")

B = Tkinter.Button(top, text ="Download TFZ", command = Download)
C = Tkinter.Button(top, text ="TFZ to TFM", command = Decompress)
D = Tkinter.Button(top, text ="TFM to TFZ", command = Compress)
INFO = Tkinter.Button(top, text ="About", command = About)

B.pack()
C.pack()
D.pack()
canvas1.create_window(170, 130, window=INFO)
top.mainloop()
