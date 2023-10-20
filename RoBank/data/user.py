import connection as con
from model.userModel import User

class UserData():


    def __init__(self):
        try:
            self.db = con.Connection().connect()
            self.cursor = self.db.cursor()
            sql_insert = """INSERT INTO users VALUES(null, '{}', '{}', '{}')"""
            self.cursor.execute(sql_insert)
            self.db.commit()
        except Exception as Ex:
            print("User Admin already exists", Ex) 


    def login(self, user:User):
        self.db = con.Connection().connect()
        self.cursor = self.db.cursor()
        res = self.cursor.execute("SELECT * FROM users WHERE user='{}' AND key ='{}'".format(user._user, user._key))
        fila = res.fetchone()
        if fila:
            user = User(name=fila[1], user=fila[2])
            self.cursor.close()
            self.db.close()
            return user
        else:
            self.cursor.close()
            self.db.close()
            return None