import sqlite3


class Connection():
    def __init__(self):
        try:
            self.con = sqlite3.connect("bank.db")
            self.createTables()
            self.checkAdmin()
        except Exception as Ex:
            print(Ex)

    # Creando tablas:
    def createTables(self):
        sql_create_table1 = """CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, user TEXT, key TEXT)"""
        cur = self.con.cursor()
        cur.execute(sql_create_table1)
        cur.close()

    def checkAdmin(self):
        try:
            cur = self.con.cursor()
            cur.execute("SELECT COUNT(*) FROM users WHERE user='admin'")
            count = cur.fetchone()[0]
            
            cur.close()
        except Exception as Ex:
            print("Error while checking for Admin:", Ex)

    

    def connect(self):
        return self.con 


if __name__ == "__main__":
    conn = Connection()
