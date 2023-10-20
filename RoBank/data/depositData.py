import connection as con
from model.movements import DepositInter
from datetime import datetime


class DepositData():

    def __init__(self) -> None:
        try:
            self.db = con.Connection().connect()
            self.cursor = self.db.cursor()
            sql_create_deposit = """CREATE TABLE IF NOT EXISTS deposits
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            amount NUMERIC, 
            type TEXT,
            document NUMERIC,
            international BOOLEAN,
            registration_date DATETIME,            
            name TEXT, 
            lastname TEXT,             
            name TEXT,
            birthdate DATETIME,
            birthplace TEXT,
            motive TEXT,     
            sex TEXT,
            terms BOOLEAN)"""
            self.cursor.execute(sql_create_deposit)
            self.cursor.close()
            self.db.close()
            print("Table deposit created")
        except Exception as ex:
            print("Table deposit OK ", ex)

    def register(self, info: DepositInter):
        date = datetime.now().strftime("%d%m%Y %H:%M")
        self.db = con.Connection().connect()
        self.cursor = self.db.cursor()
        self.cursor.execute("""
        INSERT INTO deposits values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._amount, info._type, info._document, info._international, date, info._lastname, info._name, info._birthdate, info._birthplace, info._motive, info._sex, info._sex))
        self.db.commit()
        if self.cursor.rowcount == 1:
            return True
        else:
            return False
