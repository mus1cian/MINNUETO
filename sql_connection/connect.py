import cx_Oracle
import sql_connection.connection as conn

connection = None
try:
    connection = cx_Oracle.connect(
        conn.username,
        conn.password,
        conn.dsn,
        encoding=conn.encoding)

    # show the version of the Oracle Database
    print(connection.version)
except cx_Oracle.Error as error:
    print(error)
finally:
    # release the connection
    if connection:
        connection.close()