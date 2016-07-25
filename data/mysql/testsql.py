import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '1python1',
    'host': 'localhost',
    'database': 'testdb'
}

try:
    conn = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print "Something is wrong with your user name or password"
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print "Database does not exist"
    else:
        print err
else:
    if conn.is_connected():
        print "Connected to MySQL database"

    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()

    print "Database version : %s " % data

    conn.close()

    if not conn.is_connected():
        print "Already disconnected"
