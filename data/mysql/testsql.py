import mysql.connector
from mysql.connector import errorcode
# from time import sleep

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
            print ("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print ("Database does not exist")
        else:
            print (err)
    else:
        if conn.is_connected():
            print ("Connected to MySQL database")

        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()

        print ("Database version : %s ") % data

        menu = 0

        while menu == 0:
            print ("1 - Create table Customer\n2 - Create table Stock\n3 - Create table Orders" \
                  "\n4 - Insert data to customer\n5 - Add data to stock\n6 - Insert orders" \
                  "\n7 - Read some data\n8 - Exit\n9 - Update stock")
            choice = int(input("What do you want:"))
            print (choice)
            if choice == 1:
                create_c(cursor)
            elif choice == 4:
                insert_c(cursor, conn)
            elif choice == 7:
                read(cursor)
            elif choice == 2:
                create_s(cursor)
            elif choice == 5:
                insert_s(cursor, conn)
            elif choice == 8:
                menu = 1
            elif choice == 3:
                create_o(cursor)
            elif choice == 6:
                insert_o(cursor, conn)
            elif choice == 9:
                update_s(cursor, conn)
                # musi byc commit!
            else:
                print(" Try again.")

        input('Press anything to close database...')
        cursor.close()
        conn.close()

        if not conn.is_connected():
            print("Database disconnected")

    return


def create_c(ccursor):
    ask_create = input("Are you sure? it will delete all your data... If sure, press y...")
    if ask_create == "y":
        ccursor.execute("DROP TABLE IF EXISTS Employee")
        ccursor.execute("CREATE TABLE Employee(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25), Age INT)")


def insert_c(icursor, iconn):
    try:
        a = input("Name of customer: ")
        b = int(input("Age: "))
        new_emp = (a, b)
        sql = "INSERT INTO Employee(Name, Age) VALUES (%s, %s)"
        icursor.execute(sql, new_emp)
        iconn.commit()
    except mysql.connector.Error as err:
        print (err)
        iconn.rollback()


def read(rcursor):
    what = input("What do you want to see: 1 - Customers, 2 - Stock, 3 - Orders")
    if what == "1":
        sql_r = "SELECT * FROM Employee"
    elif what == "2":
        sql_r = "SELECT * FROM Stock"
    elif what == "3":
        sql_r = "SELECT Orders.Id, Employee.Name, Stock.Item \
        FROM Orders LEFT JOIN Employee ON Orders.Customer_Order = Employee.Id \
        LEFT JOIN Stock ON Orders.Goods_Order = Stock.Id"
    else:
        print ("Wrong option chosen. Default query will be used..")
        sql_r = "SELECT * FROM Employee"
    try:
        rcursor.execute(sql_r)
        print ("%-10s %s") % (rcursor.description[1][0], rcursor.description[2][0])
        row = rcursor.fetchone()
        while row is not None:
            print ("%-10s %s") % (row[1], row[2])
            row = rcursor.fetchone()
    except mysql.connector.Error as err:
        print (err)


def create_s(scursor):
    ask_create = input("Are you sure? it will delete all your data... If sure, press y...")
    if ask_create == "y":
        scursor.execute("DROP TABLE IF EXISTS Stock")
        scursor.execute("CREATE TABLE Stock(Id INT PRIMARY KEY AUTO_INCREMENT, Item VARCHAR(25), Amount INT)")


def insert_s(icursor, iconn):
    try:
        a = input('Name of a product: ')
        b = int(input("Number of items: "))
        new_item = (a, b)
        sql = "INSERT INTO Stock(Item, Amount) VALUES (%s, %s)"
        icursor.execute(sql, new_item)
        iconn.commit()
    except mysql.connector.Error as err:
        print (err)
        iconn.rollback()


def create_o(ocursor):
    ask_create = input("Are you sure? it will delete all your data... If sure, press y...")
    if ask_create == "y":
        try:
            ocursor.execute("DROP TABLE IF EXISTS Orders")
        except mysql.connector.Error as err:
            print (err)

        ocursor.execute("CREATE TABLE Orders(Id INT PRIMARY KEY AUTO_INCREMENT, Customer_Order INT, Goods_Order INT, \
        CONSTRAINT customer_fk FOREIGN KEY (Customer_Order) REFERENCES Employee (Id), \
        CONSTRAINT stock_fk FOREIGN KEY (Goods_Order) REFERENCES Stock (Id))")


def insert_o(ocursor, oconn):
    try:
        a = int(input('Customer: '))
        b = int(input('Goods: '))
        new_item = (a, b)
        sql = "INSERT INTO Orders(Customer_Order, Goods_Order) VALUES (%s, %s)"
        ocursor.execute(sql, new_item)
        oconn.commit()
    except mysql.connector.Error as err:
        print (err)
        oconn.rollback()


def update_s(cursor, conn):
    pass

start()
