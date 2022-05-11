# coding: utf-8
 
# Encoder Transformice password
# Author: Xset
# Thanks for the scrypt Weslei.
 
import mimetypes
import hashlib
import gzip,zlib
import base64
import binascii
import sys
 
class CreateHash():
   
    def crypte(self, password):
       
        saltbytes = [-9, 25, -92, -37, -117, 18, 112, -95, -5,
        -108, 40, -83, -107, 73, -92, -102, 46, -52, 49, -118, -79,
        -56, -72, 63, -69, -98, -118, -22, 46, -16, -22, -111];
        hash=hashlib.sha256(str(password).encode('ISO8859_1')).hexdigest()
        h=[]
       
        for b in range(0,len(hash)):
            h.append(ord(hash[b]))
        for b in range(0,len(saltbytes)):
            h.append(saltbytes[b]+b)
        hexstring=''
       
        for b in range(0,len(h)):
            test=self.toHex(h[b],True,2)[4:]
            hexstring+=test
         
        unhexlify=binascii.unhexlify(hexstring)
 
        unhexlifyhashed=(hashlib.sha256(unhexlify).hexdigest())
       
        stringbase64HashedOfHashedPwAndSalt=(base64.b64encode(binascii.unhexlify(unhexlifyhashed)))
 
 
        return stringbase64HashedOfHashedPwAndSalt
 
 
    def toHex(self, h,f,b):
        e = "0123456789abcdef";
        d = "";
        if (f) :
            for c in range(0,4) :
                d += e[(h >> ((3 - c) * 8 + 4)) & 15] + e[(h >> ((3 - c) * 8)) & 15]
        else :
            for a in range(0,4) :
                d += e[(h >> (a * 8 + 4)) & 15] + e[(h >> (a * 8)) & 15]
        if (b) :
             return d[b:]
        return d
 
Password = "test1234" # Password
self = CreateHash()
hashpassword = self.crypte(Password)
 
fo = open("foo.txt", "w")
fo.write( str(hashpassword) )
fo.close()
 
print(hashpassword)
raw_input()