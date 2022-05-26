import cx_Oracle
import sql_connection.connection as conn

class SQLConnection:
    def __init__ (self, root):
        self.root = root
        self.con = cx_Oracle.connect(conn.username, conn.password, conn.dsn, encoding=conn.encoding)
        self.cur = self.con.cursor()
        
    def getConnection(self):
        return self.cur, self.con
    
    def openConnection(self):
        self.con = cx_Oracle.connect(conn.username, conn.password, conn.dsn, encoding=conn.encoding)
        self.cur = self.con.cursor()