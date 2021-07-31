import MySQLdb as sql


import pymysql
 
class MyDb:

    def __init__(self):
        self.schema="pingerator"
        self.host=""
        self.user=""
        self.password=""

    def dbDebugDisplay(self, dbObject, statement):
        cursor = self.dbInteract(statement, dbObject)
        print(self.dbData2Array(cursor))

        
    def dbInteract(self, statment:str, dbConnection)->"Returns the cursor":
        #create cursor
        cursor = dbConnection.cursor()
        
        #execute the query
        cursor.execute(statment)
        return cursor

    def dbData2Array(self, cursor):
        tableData = cursor.fetchall()
        return tableData

    def dbConnect(self) ->"dont forget to close the connection":
        mysql_connection = pymysql.connect(self.host, self.user, self.password, self.schema)
        mysql_connection.cursor()
        return mysql_connection
    

