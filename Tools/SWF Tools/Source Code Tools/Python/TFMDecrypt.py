import struct
import zlib
import os
import urllib2
import re
import sys
import ctypes
import shutil
from datetime import datetime
from StringIO import StringIO

class main(object):
	def __init__(self):
		if len(sys.argv)>1:
			if re.search("h", sys.argv[1]):
				print """h=This Help
c=Download ChargeurTransformice.swf.swf also.
e=Do Ecimrofsnart too (TFL.swf)
d=Remove A.txt and B.txt after finished.

Example: TFMDecrypt.py ec"""
				os._exit(1)
		print "For some extra command line params, Run this in command prompt like:"
		print "TFMDecrypt.py h"
		try:
			print TFMDecrypt()
		except:
			print TFMDecrypt(True)
		try:
			os.remove("bak.swf")
		except:
			pass

class TFMDecrypt(object):
	def decompressSWF(self, f):
	   if type(f) is str:
		  f = StringIO(f)
	   f.seek(0, 0)
	   magic = f.read(3)
	   if magic == "CWS":
		  return "FWS" + f.read(5) + zlib.decompress(f.read())
	   else:
		  return None
	def compressSWF(self, f):
	   if type(f) is str:
		  f = StringIO(f)
	   f.seek(0, 0)
	   magic = f.read(3)
	   if magic == "FWS":
		  return "CWS" + f.read(5) + zlib.compress(f.read())
	   else:
		  return None
	def ByteToHex(self, byteStr):
		return ''.join([ "%02X " % ord(x) for x in byteStr]).strip()
	def HexToByte(self, hexStr):
		bytes = []
		hexStr = ''.join(hexStr.split(" "))
		for i in range(0, len(hexStr), 2):
			bytes.append(chr(int(hexStr[i:i+2], 16)))
		return ''.join(bytes)
	def getReadConstString(self, ConstHex, DecompSWF):
		if type(ConstHex)==int:
			ConstHex=self.makeABC(ConstHex)
		ConstHex="\x5E"+ConstHex+"\x2C"
		DsIO=StringIO(DecompSWF)
		Find=DecompSWF.find(ConstHex)+4
		DsIO.read(Find)
		DsBytes=DsIO.read(2)
		return DsBytes
	def read8(self, byte):
		try:
			byte ,= struct.unpack('>B', struct.pack('>B', int('0x'+byte,16)))
		except ValueError:
			return byte
		return byte
	def readABC(self, file, bits, sign):
		byte = self.read8(file[:2])
		if not byte & 0x00000080:
			return byte
		byte = byte & 0x0000007f | self.read8(file[2:4])<<7
		if not byte & 0x00004000:
			return byte
		byte = byte & 0x00003fff | self.read8(file[4:6])<<14
		if not byte & 0x00200000:
			return byte
		byte = byte & 0x001fffff | self.read8(file[6:8])<<21
		if not byte & 0x10000000:
			return byte
		byte = byte & 0x0fffffff | self.read8(file[8:10])<<28
		return byte
	def binb(self, num):
		bits = []
		negative = num < 0
		n = abs(num)
		while not bits or n:
				n, bit = divmod(n,2)
				bits.append(str(bit))
		bits.reverse()
		binary = int("".join(bits))
		return(str(binary))
	def makeABC(self, num):
		abc = ''
		binlist = []
		mybin = self.binb(num)
		if mybin[0:1] == '-':
				mybin = mybin[1:]
		while len(mybin) > 0:
				if len(mybin) > 7:
						binlist.append('1'+mybin[-7:])
						mybin = mybin[:-7]
				else:
						binlist.append('0'*(8-len(mybin))+mybin)
						mybin = ''
		for mybin in binlist:
				binh = hex(int(mybin,2))
				abc = abc+'0'*(2-len(binh[2:]))+binh[2:]
		return self.HexToByte(abc)
	def read8C(self, file):
		byte ,= struct.unpack('>B',file.read(1))
		return byte
	def readABCC(self, file, bits, sign):
		byte = self.read8C(file)
		if not byte & 0x00000080:
			if (sign == 's'):
				byte = ctypes.c_long(byte).value
			return byte
		byte = byte & 0x0000007f | self.read8C(file)<<7
		if not byte & 0x00004000:
			if sign == 's':
				byte = ctypes.c_long(byte).value
			return byte
		byte = byte & 0x00003fff | self.read8C(file)<<14
		if not byte & 0x00200000:
			if sign == 's':
				byte = ctypes.c_long(byte).value
			return byte
		byte = byte & 0x001fffff | self.read8C(file)<<21
		if not byte & 0x10000000:
			if sign == 's':
				byte = ctypes.c_long(byte).value
			return byte

		byte = byte & 0x0fffffff | self.read8C(file)<<28
		if sign == 's':
			byte = ctypes.c_long(byte).value
		return byte
	def fillPools(self, SWF, reverseSearch=False, IgnoreOtherThings=True):
		intTmp=[]
		uintTmp=[]
		doubleTmp=[]
		stringTmp=[]
		namespaceTmp=[]
		ns_setTmp=[]
		multinameTmp=[]
		cpools=[]
		file = StringIO(SWF)
		file.seek(0,2)
		end = file.tell()
		file.seek(0)
		magic = "\x10\x00\x2E\x00"
		cpools = []
		print str(datetime.today()),"Searching for constant pools..."
		file.seek(0)
		if reverseSearch:
			PriPosSe=len(SWF)-(SWF[::-1].find("\x00\x2E\x00\x10")+40)
			SKIPHERE=SWF.find(magic, PriPosSe)
		else:
			SKIPHERE=SWF.find(magic)
		for i in range(SKIPHERE, end):
			file.seek(i)
			if file.read(4) == magic:
				cpseek = file.tell()
				file.seek(cpseek-11)
				if file.read(5) == 'frame':
					cpools.append(cpseek)
		if len(cpools) == 0:
			print str(datetime.today()),'No constant pools found.'
			return False
		print str(datetime.today()),"Reading constant pools..."
		for cpseek in cpools:
			file.seek(cpseek-11)
			#print 'cpool data for',file.read(6)
			file.seek(cpseek)
			int_count = self.readABCC(file, 30, 'u')
			#print 'int index count =',int_count - 1
			hex_len = len(hex(int_count)) - 2
			for i in range(1,int_count):
				if IgnoreOtherThings:
					sint = self.readABCC(file, '32', 's')
				else:
					sint = self.readABCC(file, '32', 's')
					intTmp.append([i, sint])

			uint_count = self.readABCC(file, 30, 'u')
			#print 'uint index count =',uint_count - 1
			hex_len = len(hex(uint_count))-2
			for i in range(1,uint_count):
				if IgnoreOtherThings:
					uint = self.readABCC(file, '32', 'u')
				else:
					uint = self.readABCC(file, '32', 'u')
					uintTmp.append([i, unit])

			double_count = self.readABCC(file, 30, 'u')
			#print 'double index count =',double_count - 1
			hex_len = len(hex(double_count)) - 2
			for i in range(1,double_count):
				double = file.read(8)
				if IgnoreOtherThings:
					pass
				else:
					double = str(struct.unpack('d', double)[0])
					doubleTmp.append([i, double])

			string_count = self.readABCC(file, 30, 'u')
			#print 'string index count =',string_count - 1
			hex_len = len(hex(string_count)) - 2
			for i in range(1,string_count):
				vlen = self.readABCC(file, '40', 'u')
				string = file.read(vlen)
				stringTmp.append([i, string])

			if IgnoreOtherThings:
				pass
			else:
				namespace_count = self.readABCC(file, 30, 'u')
				#print 'namespace index count =',namespace_count - 1
				hex_len = len(hex(namespace_count)) - 2
				for i in range(1,namespace_count):
					type = self.readABCC(file, '40', 'u')
					if type == 0x05:
						type = "PrivateNs"
					if type == 0x08:
						type = "Namespace"
					if type == 0x16:
						type = "PackageNamespace"
					if type == 0x17:
						type = "PackageInternalNs"
					if type == 0x18:
						type = "ProtectedNamespace"
					if type == 0x19:
						type = "ExplicitNamespace"
					if type == 0x1A:
						type = "StaticProtectedNs"
					namespace = self.readABCC(file, 30, 'u')
					namespaceTmp.append([i, type])

				nsset_count = self.readABCC(file, 30, 'u')
				#print 'ns_set index count =',nsset_count - 1
				hex_len = len(hex(nsset_count)) - 2
				for i in range(1,nsset_count):
					ns_count = self.readABCC(file, 30, 'u')
					ns_hex_len = len(hex(ns_count))
					for i in range(0,ns_count):
						namespace = self.readABCC(file, 30, 'u')
						ns_setTmp.append([i, namespace])

				multiname_count = self.readABCC(file, 30, 'u')
				#print 'multiname index count =',multiname_count - 1
				hex_len = len(hex(multiname_count)) - 2
				for i in range(1,multiname_count):
					type = self.readABCC(file, '40', 'u')
					if type == 0x07 or type == 0x0D:
						type = "QName"
						namespace = self.readABCC(file, 30, 'u')
						name = self.readABCC(file, 30, 'u')
						multinameTmp.append([i, namespace, name, type])
					if type == 0x0F or type == 0x10:
						type = "RTQName"
						name = self.readABCC(file, 30, 'u')
						multinameTmp.append([i, "", name, type])
					if type == 0x11 or type == 0x12:
						type = "RTQNameL"
						multinameTmp.append([i, "", "", type])
					if type == 0x09 or type == 0x0B:
						type = "Multiname"
						name = self.readABCC(file, 30, 'u')
						nsset = self.readABCC(file, 30, 'u')
						multinameTmp.append([i, nsset, name, type])
					if type == 0x1B or type == 0x1C:
						type = "MultinameL"
						nsset = self.readABCC(file, 30, 'u')
						multinameTmp.append([i, nsset, "", type])
		cpools=[intTmp,uintTmp,doubleTmp,stringTmp,namespaceTmp,ns_setTmp,multinameTmp]
		return cpools
	def getStringFromPoolNum(self, num):
		strings=self.ConstantPools[3]
		for x in strings:
			if x[0]==num:
				return x[1]
		return "None"
	def shortToInt(self, sbytes):
		try:
			#myhex = ''.join('%02x' % int(i,16) for i in ByteToHex(sbytes).replace(" ",""))
			myhex = self.ByteToHex(sbytes).replace(" ","")
		except:
			print repr(sbytes)
			print "You did not correctly type a hex or int value"
			sys.exit(1)

		if len(myhex) % 2:
			myhex = '0' + myhex
		myint = self.readABC(myhex[:10], 30, 'u')
		#print "INT:",myint
		#print "HEX:",myhex[:2],myhex[2:4],myhex[4:6],myhex[6:8],myhex[8:10]
		return myint
	def __init__(self,SWAPFi=False):
		self.UTF=""
		self.Short=0
		self.Info=[]
		self.ConstantPools=[]
		httpServerAddr="www.transformice.com"
		DEBUGGING = False
		if not SWAPFi:
			if len(sys.argv)>1:
				if re.search("c", sys.argv[1]):
					print str(datetime.today()),"Downloading ChargeurTransformice.swf.swf..."
					url = urllib2.urlopen("http://"+httpServerAddr+"/ChargeurTransformice.swf.swf")
					datas = url.read()
					fX=open('ChargeurTransformice.swf.swf', 'wb')
					fX.write(datas)
					fX.close()
			print str(datetime.today()),"Downloading Transformice.swf.swf..."
			url = urllib2.urlopen("http://"+httpServerAddr+"/Transformice.swf")#"http://94.23.8.194/Transformice.swf.swf")
			datas = url.read()
			fX=open('Transformice.swf', 'wb')
			fX.write(datas)
			fX.close()

			if len(sys.argv)>1:
				if re.search("e", sys.argv[1]):
					DecStringEci=self.decompressSWF(datas)
					self.ConstantPools=self.fillPools(DecStringEci, True)
					REPLIST=[]
					FoundFunc=False
					for x in self.ConstantPools[3]:
						if x[1].startswith("\x00"):
							fillString="A"+str(x[0])
							AX=fillString+''.join(["A" for p in range(len(fillString),len(x[1]))])
							REPLIST.append([x[1], AX])
					for x in REPLIST:
						DecStringEci=DecStringEci.replace(x[0],x[1])
					TFM=open('TFL.swf', 'wb')
					TFM.write(DecStringEci)
					TFM.close()
			shutil.copy("Transformice.swf","bak.swf")
		else:
			try:
				shutil.copy("bak.swf","Transformice.swf")
			except:
				print str(datetime.today()),"Downloading Transformice.swf.swf..."
				url = urllib2.urlopen("http://"+httpServerAddr+"/Transformice.swf")
				datas = url.read()
				fX=open('Transformice.swf', 'wb')
				fX.write(datas)
				fX.close()
		Files=[]
		FileA=""
		FileB=""
		FileC=""
		x=0
		DFile = open("./Transformice.swf", "rb")
		string = DFile.read()
		if string[:3]=="CWS":
			string = self.decompressSWF(string)
		DFile.close()
		#os.remove("./Transformice.swf.swf")
		if not DEBUGGING:
			DBG=open('Decompressed.dat', 'wb')
			DBG.write(string)
			DBG.close()
		while x<3:
			PIO = StringIO(string)
			PriPos=string.find(chr(x+1)+"\x00\x00\x00\x00\x00")
			PIO.read(PriPos-6)
			S=PIO.read(6)
			Head=S[:2];Len=struct.unpack("!l", S[2:][::-1])[0]
			print repr(S)
			FileA=PIO.read(Len)
			if DEBUGGING:
				DBG=open(str(x)+'.dat', 'wb')
				DBG.write(FileA[6:])
				DBG.close()
				DBG=open('F'+str(x)+'.dat', 'wb')
				DBG.write(FileA)
				DBG.close()
			Files.append(FileA[6:])
			string=string.replace(FileA,"")
			if DEBUGGING:
				DBG=open('R'+str(x)+'.dat', 'wb')
				DBG.write(string)
				DBG.close()
			x+=1
			if FileA[6:].startswith("CWS"):
				print 'swf is ' + str(x)
			elif FileA[6:].startswith("FWS"):
				print 'swf is ' + str(x)
		compressed=False
		for y in Files:
			if y.startswith("CWS"):
				compressed=True
				FileA=y
				Files.remove(y)
				break;
			if y.startswith("FWS"):
				compressed=False
				FileA=y
				Files.remove(y)
				break;
		try:
			if compressed:
				self.decompressSWF(FileA+Files[0]+Files[1])
				FileB=Files[0]
				FileC=Files[1]
				print 'order is 0 + 1 + Swf'
			else:
				self.compressSWF(FileA+Files[0]+Files[1])
				FileB=Files[0]
				FileC=Files[1]
				print 'order is 0 + 1 + Swf'
		except:
			if compressed:
				self.decompressSWF(FileA+Files[1]+Files[0])
				FileB=Files[1]
				FileC=Files[0]
				print 'order is 1 + 0 + Swf'
			else:
				self.compressSWF(FileA+Files[0]+Files[1])
				FileB=Files[0]
				FileC=Files[1]
				print 'order is 1 + 0 + Swf'
		TFM2=open('Transformicee.swf', 'wb')
		TFM=open('Transformice (Decrypted).swf', 'wb')
		
		if compressed:
			TFM.write(self.decompressSWF(FileA+FileB+FileC))
			TFM2.write(self.decompressSWF(FileA+FileB+FileC))
			print 'order is A + B + C'
		else:
			if SWAPFi:
				TFM.write(FileA+FileC+FileB)
				TFM2.write(FileA+FileC+FileB)
				print 'order is A + C + B'
			else:
				TFM.write(FileA+FileB+FileC)
				TFM2.write(FileA+FileB+FileC)
				print 'order is A + B + C'
		TFM.close()
		TFM2.close()
		DFile = open("./Transformice (Decrypted).swf", "rb")
		DecString = DFile.read()
		DecompSWF=DecString
		DFile.close()
		#os.remove("./Transformice (Decrypted).swf")
		self.ConstantPools=self.fillPools(DecString)
		REPLIST=[]
		DFile = open("./A.txt", "wb")
		FoundFunc=False
		for x in self.ConstantPools[3]:
			DFile.write(repr(x)+"\n")
			if x[1].startswith("\x00"):
				fillString="A"+str(x[0])
				AX=fillString+''.join(["A" for p in range(len(fillString),len(x[1]))])
				REPLIST.append([x[1], AX])
			if len(x[1])==3 and re.search("\?",x[1]) and not FoundFunc:
				FoundFunc=True
				REPLIST.append(["\x03"+x[1], "\x03"+"AZA"])
			if len(x[1])==3 and re.search("\.",x[1]) and not FoundFunc:
				FoundFunc=True
				REPLIST.append(["\x03"+x[1], "\x03"+"AZA"])
			if len(x[1])==3 and re.search("\{",x[1]) and not FoundFunc:
				FoundFunc=True
				REPLIST.append(["\x03"+x[1], "\x03"+"AZA"])
			if len(x[1])==3 and re.search("\:",x[1]) and not FoundFunc:
				FoundFunc=True
				REPLIST.append(["\x03"+x[1], "\x03"+"AZA"])
			if len(x[1])==3 and re.search("\!",x[1]) and not FoundFunc:
				FoundFunc=True
				REPLIST.append(["\x03"+x[1], "\x03"+"AZA"])
			if len(x[1])==3 and re.search("\/",x[1]) and not FoundFunc:
				FoundFunc=True
				REPLIST.append(["\x03"+x[1], "\x03"+"AZA"])
			if len(x[1])==3 and re.search("\,",x[1]) and not FoundFunc:
				FoundFunc=True
				REPLIST.append(["\x03"+x[1], "\x03"+"AZA"])
			if len(x[1])==3 and re.search("\'",x[1]) and not FoundFunc:
				FoundFunc=True
				REPLIST.append(["\x03"+x[1], "\x03"+"AZA"])
			if len(x[1])==3 and re.search("\(",x[1]) and not FoundFunc:
				FoundFunc=True
				REPLIST.append(["\x03"+x[1], "\x03"+"AZA"])
		DFile.close()
		DFile = open("./B.txt", "wb")
		for x in REPLIST:
			DFile.write(repr(x)+"\n")
			DecString=DecString.replace(x[0],x[1])
		DFile.close()
		y=8 #Change this to 0 to write all the pools to files.
		while y < 7:
			DFile = open("./"+str(y)+".txt", "wb")
			for x in self.ConstantPools[y]:
				DFile.write(repr(x)+"\n")
			DFile.close()
			y+=1
		#for x in self.ConstantPools[3]:
		#	if x[1]=="AnimCourse":
		#		try:
		#			print x, DecString.count("\x2C"+self.makeABC(x[0])), repr(DecString[DecString.find("\x2C"+self.makeABC(x[0]))-5:DecString.find("\x2C"+self.makeABC(x[0]))+5])
		#		except:
		#			print "421"
		if len(sys.argv)>1:
			if re.search("d", sys.argv[1]):
				try:
					os.remove("A.txt")
				except:
					pass
				try:
					os.remove("B.txt")
				except:
					pass
		TFM=open('TFA.swf', 'wb')
		TFM.write(DecString)
		TFM.close()

if __name__ == '__main__':
	main()
