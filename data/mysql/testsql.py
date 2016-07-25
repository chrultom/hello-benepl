import mysql.connector

conn = mysql.connector.connect(host='localhost', database='testdb', user='root', password='1python1')

if conn.is_connected():
    print "Connected to MySQL database"

conn.close()

if not conn.is_connected():
    print "Already disconnected"
