import sqlite3
conn = sqlite3.connect("database1.db")
cur = conn.cursor()
cmd = input("enter command:")
cur.execute(cmd)
for i in cur.fetchall():
    print(i)
cmd1 = input("enter command to delete:")
print("Deleted")
cur.execute(cmd1)
cur.execute(cmd)
for i in cur.fetchall():
    print(i)
