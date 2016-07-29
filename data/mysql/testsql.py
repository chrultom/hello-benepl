import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '1python1',
    'host': 'localhost',
    'database': 'testdb'
}


def start():

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

        menu = 0

        while menu == 0:
            print "1 - Create, 2 - Insert, 3 - Read, 4 - Exit"
            choice = int(raw_input("What do you want:"))
            print choice
            if choice == 1:
                create(cursor)
            elif choice == 2:
                insert(cursor, conn)
            elif choice == 3:
                read(cursor)
            elif choice == 4:
                menu = 1
            else:
                print" Try again."

        raw_input('Press anything to close database...')
        cursor.close()
        conn.close()

        if not conn.is_connected():
            print "Database disconnected"

    return


def create(ccursor):
    ask_create = raw_input("Are you sure? it will delete all your data... If sure, press y...")
    if ask_create == "y":
        ccursor.execute("DROP TABLE IF EXISTS Employee")
        ccursor.execute("CREATE TABLE Employee(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25), Age INT)")


def insert(icursor, iconn):
    try:
        a = 'Kowalski'
        b = 22
        new_emp = (a,b)
        print type(new_emp[1])
        #sql = ("INSERT INTO Employee(Name, Age) VALUES ('Kowalski', 29)")
        #sql = ("""INSERT INTO Employee(Name, Age) VALUES (%s, %d)""")
        sql = ("INSERT INTO Employee(Name, Age) VALUES (%s, %s)")
        icursor.execute(sql, new_emp)
        iconn.commit()
    except mysql.connector.Error as err:
        print err
        iconn.rollback()


def read(rcursor):
    rcursor.execute("SELECT * FROM employee")
    for (row, name, age) in rcursor:
        print "%s is %d years old." % (name, age)

start()
