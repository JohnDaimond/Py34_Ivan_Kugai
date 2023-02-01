import sqlite3

database = sqlite3.connect("../database.db") ##

with open("posts.sql") as f:
    database.executescript(f.read())


cir = database.cursor()

cir.execute("INSERT INTO posts (author,title,content) VALUES(?,?,?)",
            ("IVAN","fIRST POST!","iT IS WORKED"))


cir.execute("INSERT INTO posts (author,title,content) VALUES(?,?,?)",
            ("IVAN","/SECOND POST!","hello evryone"))

database.commit()
database.close()