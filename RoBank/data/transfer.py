import connection as con
from model.movements import Transfer
from datetime import datetime


class TransData():

    def __init__(self) -> None:
        try:
            self.db = con.Connection().connect()
            self.cursor = self.db.cursor()
            sql_create_transfers = """CREATE TABLE IF NOT EXISTS transfers
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            amount NUMERIC, 
            type TEXT,
            document NUMERIC,
            international BOOLEAN,
            registration_date DATETIME, 
            verify BOOLEAN DEFAULT 'false', 
            motive TEXT)"""
            self.cursor.execute(sql_create_transfers)
            self.cursor.close()
            self.db.close()
            print("Table transfer created")
        except Exception as ex:
            print("Table transfer OK ", ex)

    def register(self, info: Transfer):
        date = datetime.now().strftime("%d%m%Y %H:%M")
        self.db = con.Connection().connect()
        self.cursor = self.db.cursor()
        self.cursor.execute("""
        INSERT INTO transfers values(null,'{}','{}','{}','{}','{}','{}','{}')
        """.format(info._amount, info._type, info._document, info._international, date, False, info._motive))
        self.db.commit()
        if self.cursor.rowcount == 1:
            return True
        else:
            return False
