import sqlite3

class DB:
    def __init__(this):
        this.Count = 1
        this.ChangeCodeMap()
        this.GetLastRow()

    def ChangeCodeMap(this):
        result = Cursor.execute("select Code from MapEditor").fetchall()
        for i in result:
            Cursor.execute("update MapEditor set Code = ? where Code = ?", [this.Count, i["Code"]])
            this.Count += 1

    def GetLastRow(this):
        id = Cursor.execute("SELECT Code FROM MapEditor ORDER BY Code DESC LIMIT 1").fetchone()["Code"]
        print("Last ID in the table is: "+str(id))
        raw_input("")

    
if __name__ == "__main__":
    Database, Cursor = None, None
    Database = sqlite3.connect("./database.db", check_same_thread = False)
    Database.text_factory = str
    Database.isolation_level = None
    Database.row_factory = sqlite3.Row
    Cursor = Database.cursor()

    DB()
