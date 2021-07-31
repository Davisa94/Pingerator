import pymysql


class DBInteract:
    def __init__(self, dbObject=""):
        self.DBO = dbObject

    def getSpeeds(self):
        sql = ("SELECT * FROM speeds")
        cursor.execute(sql)
        return dbObject