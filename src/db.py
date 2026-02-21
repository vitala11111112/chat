import sqlite3
class Users():
    def __init__(self, dbname="users.db"):
        self.dbname = dbname

        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT,chats TEXT)""")
            con.commit()



    def insert(self, name:str, password:int, chats:str):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users(name,password,chats) VALUES (?, ?, ?);",
                        (name,password,chats))
            con.commit()

    def read(self):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Users")
            return cur.fetchall()


class Chats():
    def __init__(self, dbname="chats.db"):
        self.dbname = dbname

        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS chats(
                id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,users_id)""")
            con.commit()

    def insert(self, name:str, users_id:str):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO chats(name,users_id) VALUES ( ?, ?);",
                        (name,users_id))
            con.commit()

    def read(self):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Chats")
            return cur.fetchall()








class Messeges():
    def __init__(self, dbname="messeges.db"):
        self.dbname = dbname

        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS messeges(
                id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, chat_id, user_id)""")
            con.commit()

    def insert(self, name:str, password:int, chats:str):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO messeges(name,password,chats) VALUES (?, ?, ?);",
                        (name,password,chats))
            con.commit()

    def read(self):
        with sqlite3.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Messeges")
            return cur.fetchall()

