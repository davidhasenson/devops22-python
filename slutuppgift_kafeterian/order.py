from pickle import NONE
import sqlite3

con = sqlite3.connect("slutuppgift_kafeterian\shop.db")
cur = con.cursor()

class Order:

    def __init__(self, itemid):
        self.orderid = None
        self.itemid = itemid
        self.extrasugar = None
        self.extramilk = None
        self.completed = None
        self.timestamp = None

    def __str__(self):
        return self.orderid, self.itemid, self.extrasugar, self.extramilk, self.completed, self.timestamp

    def create_table_orders(self):
            return """
                CREATE TABLE IF NOT EXISTS orders(
                    orderid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    itemid INTEGER NOT NULL,
                    extrasugar TEXT,
                    extramilk TEXT,
                    completed TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                )
                """

    def insert_into_orders(self):
            return """
                INSERT INTO orders(
                    itemid,
                    extrasugar,
                    extramilk,
                    completed
                ) 
                VALUES (?, ?, ?, ?)
                """

    def input_int(self, text):
        while True:
            try:
                input_test = int(input(text))
                print(input_test)
                return input_test
            except ValueError as v:
                print(v)
                print("You must enter an int. ")
            except Exception as e:
                print(e)

    def check_itemid(self, text):
        while True:
            try:
                itemid = self.input_int(text)
                with con:
                    cur.execute("SELECT menu.itemid FROM menu WHERE itemid = ?", (itemid,))
                    menuid_check = cur.fetchone()
                    if menuid_check or itemid == 0:     # 0 to escape loop.
                        return itemid                   # Must be itemid to return 0.
                    else:
                        print(f"{itemid} is not a menu option. ")
                        continue
            except Exception as e:
                print(e)

    def input_y_or_n(self,text):
        while True:
            try:
                input_test = input(text).lower()
                if input_test in  ("y", "n"):
                    return input_test
                print(f" {input_test} is not a choice. You must specify yes(y) or no(n)")
            except Exception as e:
                print(e) 

    def add_order(self):
        try:
            itemid = self.check_itemid("Enter item id to select beverage (0 to exit): ")
            if itemid == 0: # avoid infinite loop if menu is empty.
                return
            extrasugar = self.input_y_or_n("Do you want extra sugar?(y/n) ")
            extramilk = self.input_y_or_n("Do you want extra milk?(y/n) ")
            with con:
                cur.execute(self.create_table_orders())
                cur.execute("SELECT * FROM menu")
                cur.execute(self.insert_into_orders(), (itemid, extrasugar, extramilk, "n"))
        except Exception:
            print("Error. Could not complete order. ")

    def show_orders(self):
        try:
            with con:
                cur.execute("SELECT orders.*, menu.itemname FROM orders JOIN menu ON menu.itemid = orders.itemid WHERE completed = 'n'")
                orders = cur.fetchall()
                print("orderid  itemid  itemname  extrasugar extramilk completed timestamp")
                for i in orders:
                    orders(i[0], i[1], i[6], i[2], i[3], i[4], i[5])
        except Exception as e:
            print(e)





