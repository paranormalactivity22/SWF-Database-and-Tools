# -*- coding: cp1252 -*-
import SocketServer
import sys
import os
import MySQLdb
import base64
import zlib
import sqlite3

dbcon = None
dbcur = None
try:
    dbcon = MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='normas',port= 3306)
    dbcur = dbcon.cursor()
except MySQLdb.Error, e:
    pass

HOST = '127.0.0.1'
PORT = 7777

class TCPConnectionHandler(SocketServer.BaseRequestHandler):
    def convert(self, param1):
        param2 = "MFzg66OpuXhyjARDqlOBfKtWtwDzsg4tsIQv2"
        loc8 = 0
        loc3 = 32
        loc4 = []
        loc5 = 0
        while loc5 < loc3:
            loc4.append(loc5)
            loc4[loc5] = ord(param2[loc5]) & 31
            loc5 += 1
        loc6 = 0
        loc7 = 0
        while loc7 < len(param1):
            loc8 = ord(param1[loc7])
            if loc8 + 224:
                param1 = param1[0:loc7] + chr(loc8 ^ loc4[loc6]) + param1[loc7+1:]
            loc6 = (loc6 + 1) % loc3
            loc7 += 1
        return param1

    def parseMapXml(self, xml):
        xml = zlib.compress(xml, 4)
        xml = base64.b64encode(xml)
        xml = self.convert(xml)
        xml = base64.b64encode(xml)
        return xml
        
    def handle(self):
        data = self.request.recv(1024)
        getType = data.split("|", 1)
        if getType[0] == "mapsList":
            self.getMapsList(getType[1])
        elif getType[0] == "mapInfo":
            self.getMapInfo(getType[1])
        elif getType[0] == "mapsCount":
            self.getMapsCount(getType[1])
        elif getType[0] == "mapsCountName":
            self.getMapsCountName(getType[1])

    def getMapsCountName(self, data):
        name = data
        dbcur.execute('SELECT code FROM mapeditor WHERE name = %s', (name))
        rrfRows = dbcur.fetchall();
        self.request.send(str(len(rrfRows)))
        self.request.close()
        
    def getMapsCount(self, data):
        perm = data
        dbcur.execute('SELECT code FROM mapeditor WHERE perma = %s', (int(perm)))
        rrfRows = dbcur.fetchall();
        self.request.send(str(len(rrfRows)))
        self.request.close()

    def getMapsList(self, data):
        result = ""
        perm, page, name = data.split("|")
        end = 28*int(page)
        start = end-28
        
        if name == "None":
            dbcur.execute('SELECT code, name, yesvotes, novotes, mapxml FROM mapeditor WHERE perma = %s ORDER By code DESC LIMIT %s, %s', (int(perm), start, end))
            rrf = dbcur.fetchall()
            count = 0
            for values in rrf:
                count += 1
                if count > 28:
                   break
                else:
                    result += "$7$"
                    code = values[0]
                    name  = values[1]
                    yesvotes = int(values[2])
                    novotes = int(values[3])
                    mapxml = values[4]
                    if yesvotes < 1:
                        yesvotes = 1
                    if novotes < 1:
                        novotes = 1
                    votes = yesvotes + novotes
                    rating = 1.0 * yesvotes / votes * 100

                    result += "|".join(map(str, [code, name, votes, str(rating).split(".")[0], 0, self.parseMapXml(mapxml), 0]))
        else:
            dbcur.execute('SELECT code, name, yesvotes, novotes, mapxml, perma FROM mapeditor WHERE name = %s ORDER By code DESC LIMIT %s, %s', (name, start, end))
            rrf = dbcur.fetchall()
            count = 0
            for values in rrf:
                count += 1
                if count > 28:
                   break
                else:
                    result += "$7$"
                    code = values[0]
                    name  = values[1]
                    yesvotes = int(values[2])
                    novotes = int(values[3])
                    mapxml = values[4]
                    perma = values[5]
                    if yesvotes < 1:
                        yesvotes = 1
                    if novotes < 1:
                        novotes = 1
                    votes = yesvotes + novotes
                    rating = 1.0 * yesvotes / votes * 100

                    result += "|".join(map(str, [code, name, votes, str(rating).split(".")[0], 0, self.parseMapXml(mapxml), perma]))
            
        result = result[3:]
        
        self.request.send(result)
        self.request.close()

    def getMapInfo(self, data):
        code = data
        if code.startswith("@"):
            code = code[1:]
        dbcur.execute('SELECT name, perma, mapxml, yesvotes, novotes FROM mapeditor WHERE code = %s', (code))
        values = dbcur.fetchone()

        if values == None:
            result = "None"
        else:
            name = values[0]
            perma = values[1]
            mapxml = values[2]
            yesvotes = int(values[3])
            novotes = int(values[4])
            if yesvotes < 1:
                yesvotes = 1
            if novotes < 1:
                novotes = 1
            votes = yesvotes + novotes
            rating = 1.0 * yesvotes / votes * 100

            permname = "Standard Maps"
            perms = {"0":"Standard Maps", "1":"Protected Maps", "3":"Prime Bootcamps Maps", "4":"Shaman Maps", "5":"Art Maps", "6":"Mechanism Maps", "7":"No Shaman Maps", "8":"Shaman Co-op Maps", "9":"Miscellaneous Maps", "10":"Survivor Maps", "11":"Vampire Maps", "13":"Bootcamp Maps", "17":"Racing Maps", "18":"Defilante Maps", "19":"Music Maps", "22":"Tribe House Maps", "32":"Dual Shaman Maps", "41":"Minigames Maps", "42":"Racing Test Maps", "44":"Deleted Maps"}
            if (perms.has_key(perma)):
                permname = perms[perma]

            result = "|".join(map(str, [self.parseMapXml(mapxml).replace("+", "%2B"), votes, str(rating).split(".")[0], permname, perma, name]))

        self.request.send(result)
        self.request.close()
        
class Server(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)

if __name__ == "__main__":
    server = Server((HOST, PORT), TCPConnectionHandler)
    os.system("title TFMApi")
    os.system("color A")
    print "="*80 + ("By Weeslleeyone").center(79)
    print "="*80
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
