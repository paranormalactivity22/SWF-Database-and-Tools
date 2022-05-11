import os, time, re

class Strein:
    def Start(this):
	print "Copyright 2017 Strein -> www.aulamice.com"
        try:
            dosya = open("158.swf")
            dosya.close()

            print "PARSING..."
            os.system("abcexport 158.swf")
            os.system("rabcdasm 158-0.abc")

            find = False
            print "IP FINDING IN CLASSES..."
            for fileName in os.listdir("./158-0/"):
                if fileName.endswith("asasm"):
                    with open("./158-0/"+fileName) as f:
                        for line in f:
                            ipList = re.findall("(?:[0-9]{1,3}\\.){3}[0-9]{1,3}", line)

                            if not find:
                                if len(ipList) > 0:
                                    if not ipList[0].startswith("192.168.0.1"):
                                        print "IP: [%s]" %(ipList[0])
                                        find = True

        except Exception as error:
            print "ERROR: %s" %(error)
			
os.system("title SWF IP FIND BY STREIN(TFM)")
Strein().Start()