#coding: utf-8
import sqlite3, os, re

dbcon = sqlite3.connect("./database.sqlite") # Link da DB
dbcon.isolation_level = None
dbcur = dbcon.cursor()
dbcon.row_factory = sqlite3.Row
dbcon.text_factory = str

class Maps:
    def __init__(self):
        self.lastMap = int(self.getLastCode())+1
        self.name = "Emulator" 
        self.perma = "0"
        self.path = "maps.txt"
        self.getMaps()

    def getMaps(self):
        print('Export maps...')
        mapXml = "@NoCode"
        xWrite = open(self.path+'', 'r')
        xUrl = xWrite.read()
        xWrite.close()
        for xml in re.findall('xml: <C>(.*?)</C>', xUrl):
            try:
                xml = '<C>'+xml+'</C>'
                self.lastMap += 1
                print("Exporting map %s to %s - p%s" % (str(mapXml), str(self.lastMap), self.perma))
                self.exportMap(self.name, self.lastMap, xml, 0, 0, self.perma, "0")
                self.setSetting()
            except:
                print("FAIL - export map %s to %s - p%s" % (str(mapXml), str(self.lastMap), self.perma))

    def setSetting(self):
        dbcur.execute('UPDATE settings SET value = ? WHERE setting = ?', [str(self.lastMap), "LastEditorMapCode"])
        
    def exportMap(self, name, code, values, y, n, perma, deleted):
        dbcur.execute("INSERT INTO maps (name, code, mapxml, yesvotes, novotes, perma, deleted) values (?, ?, ?, ?, ?, ?, ?)", (name, code, values, y, n, perma, deleted))
        
    def getLastCode(self):
        dbcur.execute('select value from settings where setting = ?', ["LastEditorMapCode"])
        dbcon.commit()
        rrf = dbcur.fetchone()
        if rrf is None:
                return '0'
        else:
                return rrf[0]
if __name__ == "__main__":
    os.system('title Importing...')
    Maps()
              
    raw_input('\nMapas exportados, press enter key to exit')
