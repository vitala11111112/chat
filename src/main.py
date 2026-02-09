import sqlite3
class University():
    def __init__(self, dbname="university.db"):
        self.dbname = dbname

        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS university(
                id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT)""")
            con.commit()

    def insert(self, id:int, name:str, password:int):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO university(name,password) VALUES (?, ?);",
                        (name,password))
            con.commit()

    def read(self):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM university")
            return cur.fetchall()

