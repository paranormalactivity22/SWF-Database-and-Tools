import zlib
import argparse
import os
import sys
import time
from StringIO import StringIO

dlogs=[]

def decompressSWF(f):
   if type(f) is str:
      f = StringIO(f)
   f.seek(0, 0)
   magic = f.read(3)
   if magic == "CWS":
      return "FWS" + f.read(5) + zlib.decompress(f.read())
   else:
      return None

def compressSWF(f):
   if type(f) is str:
      f = StringIO(f)
   f.seek(0, 0)
   magic = f.read(3)
   if magic == "FWS":
      return "CWS" + f.read(5) + zlib.compress(f.read())
   else:
      return None

def open_it():
    master = Tk()
    master.withdraw()
    filename = tkFileDialog.askopenfilename()
    master.quit()
    return filename

def save_as():
    master = Tk()
    master.withdraw()
    filename = tkFileDialog.asksaveasfilename()
    master.quit()
    return filename

def main(arg1, arg2=False, arg3=False):
    try:
        Type = int(arg1[0])
    except:
        print "Error! Input not a number."
        os._exit(1)
    if arg2!=False:
        if arg2=="":
            os._exit(0)
    if Type==1:
        if arg2!=False:
            data = decompressSWF(file(arg2, 'rb').read())
        else:
            data = decompressSWF(file('In.swf', 'rb').read())
    else:
        if arg2!=False:
            data = compressSWF(file(arg2, 'rb').read())
        else:
            data = compressSWF(file('In.swf', 'rb').read())
    if data:
        if arg3:
            f=open(save_as(), 'wb')
            f.write(data)
            f.close()
        else:
            f=open('Out.swf', 'wb')
            f.write(data)
            f.close()
        print "Wrote %d bytes." % (len(data))
    else:
        print "An error occured when compessing/decompressing the file. Check file type?"

if __name__ == "__main__":
    if len(sys.argv)>1:
        parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description='SWF Compressor/Decompressor', epilog="Example usage:\nSWFCompression.py -i 1")
        parser.add_argument('-i', type=str, nargs="+", required=True, help='Type. 1=Decompress. 2=Compress.\n\nInput file must be named "In.swf"\nOutput file will be named "Out.swf"')
        args = parser.parse_args()
        arg1=args.i
        main(arg1)
    else:
        from Tkinter import *
        import tkFileDialog
        print "Run this from command line and use -h to see command line options/help!\nOr just continue running it this way.\n"
        I=raw_input("1: Decompress SWF\n2: Compress SWF\nD: Cancel\n> ")
        if I=="1":
            main([1], open_it(), True)
        elif I=="2":
            main([2], open_it(), True)
        else:
            os._exit(0)
