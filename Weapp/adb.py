import sqlite

def sqcon():
    username = input("Enter username:")
    password = input("Enter password:")
    conn = sqlite3.connect('appdb.db')
    cur = conn.cursor()
    cur.execute("SELECT * from users where username = ? AND password = ?", (username,password,))
    results = cur.fetchall()
    if not results:
        print("Incorrect password, Please try again")
    else:
        print("Welcome to your page")   
    conn.close()

sqcon()
