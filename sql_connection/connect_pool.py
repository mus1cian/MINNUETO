import cx_Oracle
import sql_connection.connection as conn

# Create the session pool
pool = cx_Oracle.SessionPool(
    conn.username,
    conn.password,
    conn.dsn,
    min=100,
    max=100,
    increment=0,
    encoding=conn.encoding
)

# Acquire a connection from the pool
connection = pool.acquire()

# Use the pooled connection
print('Using the connection')

# Release the connection to the pool
pool.release(connection)

# Close the pool
pool.close()