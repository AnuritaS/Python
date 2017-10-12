'''Write a python program to query the metadata of a database
a.	List all the tables in the database
b.	For each table, list all the column names, description and data types'''
import sqlite3
db=input("Enter database name:")
conn=sqlite3.connect(db)
cur=conn.cursor()
print("Tables with information")
cmd="select name from sqlite_master where type = 'table' ORDER BY name"
cur.execute(cmd)
for i in cur.fetchall():
    print(i)
    cur.execute("pragma table_info(%s)"% i)
    for i in cur.fetchall():
        print(i)
