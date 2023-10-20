import connection as con


class CityData():
    def CityList(self):
        self.db = con.Connection().connect()
        self.cursor = self.db.cursor()
        res = self.cursor.execute(
            "SELECT * FROM citys ORDER BY name")
        citys = res.fetchall()
        return citys
