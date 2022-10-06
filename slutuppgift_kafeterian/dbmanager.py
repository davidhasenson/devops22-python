import sqlite3, csv, random
from prettytable import from_db_cursor

con = sqlite3.connect("slutuppgift_kafeterian\shop.db")
cur = con.cursor()

class Dbmanager:

    def __init__(self) -> None:
        pass

    def create_table_menu(self):
        return """
            CREATE TABLE IF NOT EXISTS menu(
                Itemid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                Itemname TEXT UNIQUE,
                Description TEXT
            )
            """

    def insert_into_menu(self):
        return """
            INSERT INTO menu(
                Itemname,
                Description
            ) 
            VALUES (?, ?)
            """

    def create_table_orders(self):
        return """
            CREATE TABLE IF NOT EXISTS orders(
                Orderid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                Itemid INTEGER NOT NULL,
                Extrasugar TEXT,
                Extramilk TEXT,
                Sugarfree TEXT,
                Decaffeinated TEXT, 
                Lactosefree TEXT,
                Status TEXT,
                Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
            )
            """

    def insert_into_orders(self):
        return """
            INSERT INTO orders(
                Itemid,
                Extrasugar,
                Extramilk,
                Sugarfree,
                Decaffeinated, 
                Lactosefree,
                Status
                
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """

    def import_csv_file_to_db(self):
        try:   
            path = input("Enter file path: ")
            with open(path, "r") as file:
                reader = csv.reader(file)
                with con:
                    cur.execute(self.create_table_menu())
                    for row in reader:
                        cur.execute(self.insert_into_menu(), row)
                    print("The file has been imported. ")
        except Exception:
            print("Importing file failed. ")

    def view_menu(self):
        try:
            with con:
                cur.execute("SELECT * FROM menu")
                formatedtable = from_db_cursor(cur)
                print(formatedtable)
                # menu = cur.fetchall()
                # print(f"\n  Item id \t Item name \t  Description ")
                # for i in menu:
                #     print(f"\t{i[0]} \t {i[1]} \t {i[2]}")
        except Exception:
            print("Error. Can't show menu. ")

    def add_menu_item(self):
        try:
            itemname = input("Enter item name: ")
            with con:
                cur.execute("SELECT menu.itemname FROM menu WHERE itemname = ?", (itemname,))
                menuid_check = cur.fetchone()
                if menuid_check:     # 0 to escape loop.
                    print("The item already exists. ")
                    return
                description = input("Enter item description: ")
                cur.execute(self.create_table_menu())        
                cur.execute(self.insert_into_menu(), (itemname, description))
        except Exception:
            print("Error. Could not add menu item. ")

    def delete_menu_item(self):
        try:
            itemid = self.check_itemid("Enter item id for deletion. 0 to exit ")
            if itemid == 0:
                return
            cur.execute("DELETE FROM menu WHERE itemid = ?", (itemid,))       #https://www.w3schools.com/sql/sql_delete.asp
        except Exception as e:
            print(e)

    def add_order(self):
        try:
            itemid = self.check_itemid("Enter item id to select beverage (0 to exit): ")
            if itemid == 0: # avoid infinite loop if menu is empty.
                return
            extrasugar = self.input_y_or_n("Do you want extra sugar?(y/n) ")
            extramilk = self.input_y_or_n("Do you want extra milk?(y/n) ")
            sugarfree = self.input_y_or_n("Do you want sugar free?(y/n) ")
            decaffeinated = self.input_y_or_n("Do you want decaffeinated?(y/n) ")
            lactosefree = self.input_y_or_n("Do you want lactosefree?(y/n) ")
            with con:
                cur.execute(self.create_table_orders())
                #cur.execute("SELECT * FROM menu")
                cur.execute(self.insert_into_orders(), (itemid, extrasugar, extramilk, sugarfree, decaffeinated, lactosefree, "Received"))
        except Exception:
            print("Error. Could not complete order. ")

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

    def input_y_or_n(self,text):
        while True:
            try:
                input_test = input(text).lower()
                if input_test in  ("y", "n"):
                    return input_test
                print(f" {input_test} is not a choice. You must specify yes(y) or no(n)")
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

    def get_itemname(self, text):
        while True:
            try:
                itemid = self.input_int(text)
                print(f"itemid {itemid} ")
                cur.execute("SELECT menu.itemname FROM menu WHERE itemid = ?", (itemid,))
                menuid_check = cur.fetchone()
                menuid_check = menuid_check[0]
                print(f"menuid_check {menuid_check} ")
                if menuid_check == itemid:
                    return menuid_check
                print(f"{itemid} is not a menu option. ")
            except Exception as e:
                print

    def check_itemid_2(self, text):     # An alternative solution to check_itemid
        while True:
            try:
                itemid = self.input_int(text)
                print(f"itemid == {itemid} ")
                if itemid == 0:
                    return itemid
                cur.execute("SELECT menu.itemid FROM menu WHERE itemid = ?", (itemid,))
                menuid_check = cur.fetchone()
                print(f"menuid_check == {menuid_check} ")
                if menuid_check != None:
                    menuid_check = menuid_check[0]
                    print(f"menuid_check == {menuid_check} ")
                    if menuid_check == itemid:
                        return menuid_check
                print(f"{itemid} isn't a menu option. ")
            except Exception as e:
                print(e)

    def check_orderid(self, text):
        while True:
            try:
                orderid = self.input_int(text)
                #print(f"itemid {itemid} ")
                cur.execute("SELECT orders.orderid FROM orders WHERE orderid = ?", (orderid,))
                menuid_check = cur.fetchone()
                #print(menuid_check)
                if menuid_check or orderid == 0:     # 0 to escape loop.
                    return orderid                   # Must be itemid to return 0.
                else:
                    print(f"{orderid} is not an order id. ")
                    continue
            except Exception as e:
                print(e)

    def order_received(self):
        try:
            orderid = self.check_orderid("Enter order id to mark as received. (0 to exit): ")
            if orderid == 0:
                return
            cur.execute("UPDATE orders SET Status = 'Received' WHERE orderid = ?", (orderid,))       #https://www.w3schools.com/sql/sql_update.asp
        except Exception as e:
            print(e)

    def order_finished(self):
        try:
            orderid = self.check_orderid("Enter order id to mark as finishad. (0 to exit): ")
            if orderid == 0:
                return
            cur.execute("UPDATE orders SET Status = 'Finished' WHERE orderid = ?", (orderid,))       #https://www.w3schools.com/sql/sql_update.asp
        except Exception as e:
            print(e)

    def order_served(self):
        try:
            orderid = self.check_orderid("Enter order id to mark as served. (0 to exit): ")
            if orderid == 0:
                return
            cur.execute("UPDATE orders SET Status = 'Served' WHERE orderid = ?", (orderid,))       #https://www.w3schools.com/sql/sql_update.asp
        except Exception as e:
            print(e)
      
    def delete_order(self):
        try:
            orderid = self.check_orderid("Enter order id for deletion. (0 to exit): ")
            if orderid == 0:
                return
            cur.execute("DELETE FROM orders WHERE orderid = ?", (orderid,))       #https://www.w3schools.com/sql/sql_delete.asp
        except Exception as e:
            print(e)

    def random_beverage(self):
        try:
            with con:              
                cur.execute("SELECT COUNT(itemid) FROM menu")  # https://www.w3schools.com/sql/sql_count_avg_sum.asp
                count = cur.fetchone()[0]
                if not count:
                    print("Error. The menu is empty. ")
                    return
                itemid = random.randint(1, count)
                extrasugar = random.choice(["y", "n"])
                extramilk = random.choice(["y", "n"])
                sugarfree = random.choice(["y", "n"])
                decaffeinated = random.choice(["y", "n"])
                lactosefree = random.choice(["y", "n"])
                cur.execute(self.create_table_orders())
                cur.execute("SELECT * FROM menu")
                cur.execute(self.insert_into_orders(), (itemid, extrasugar, extramilk, sugarfree, decaffeinated, lactosefree, "Received"))
                print("A random order was added. ")
        except Exception:
            print("Error. Could not complete order. ")

    def show_all_orders(self):
        try:
            with con:
                cur.execute("SELECT orders.*, menu.itemname FROM orders JOIN menu ON menu.itemid = orders.itemid")
                formatedtable = from_db_cursor(cur)
                print(formatedtable)
                # orders = cur.fetchall()
                # print("orderid  itemid  itemname  extrasugar extramilk sugarfree decaffeinated lactosefree \t status \t timestamp ")
                # for i in orders:
                #     print(f"{i[0]} \t {i[1]} \t {i[9]} \t {i[2]}  \t {i[3]} \t {i[4]} \t\t {i[5]} \t\t {i[6]} \t {i[7]} \t {i[8]} ")
        except Exception as e:
            print(e)

    def show_received_orders(self):
        try:
            with con:
                cur.execute("SELECT orders.*, menu.itemname FROM orders JOIN menu ON menu.itemid = orders.itemid WHERE Status = 'Received'")
                formatedtable = from_db_cursor(cur)
                print(formatedtable)
                # orders = cur.fetchall()
                # print("orderid  itemid  itemname  extrasugar extramilk sugarfree decaffeinated lactosefree \t status \t timestamp ")
                # for i in orders:
                #     print(f"{i[0]} \t {i[1]} \t {i[9]} \t {i[2]}  \t {i[3]} \t {i[4]} \t\t {i[5]} \t\t {i[6]} \t {i[7]} \t {i[8]} ")
        except Exception as e:
            print(e)

    def show_finished_orders(self):
        try:
            with con:
                cur.execute("SELECT orders.*, menu.itemname FROM orders JOIN menu ON menu.itemid = orders.itemid WHERE Status = 'Finished'")
                formatedtable = from_db_cursor(cur)
                print(formatedtable)
                # orders = cur.fetchall()
                # print("orderid  itemid  itemname  extrasugar extramilk sugarfree decaffeinated lactosefree \t status \t timestamp ")
                # for i in orders:
                #     print(f"{i[0]} \t {i[1]} \t {i[9]} \t {i[2]}  \t {i[3]} \t {i[4]} \t\t {i[5]} \t\t {i[6]} \t {i[7]} \t {i[8]} ")
        except Exception as e:
            print(e)

    def show_served_orders(self):
        try:
            with con:
                cur.execute("SELECT orders.*, menu.itemname FROM orders JOIN menu ON menu.itemid = orders.itemid WHERE Status = 'Served'")
                formatedtable = from_db_cursor(cur)
                print(formatedtable)
                # orders = cur.fetchall()
                # print("orderid  itemid  itemname  extrasugar extramilk sugarfree decaffeinated lactosefree \t status \t timestamp ")
                # for i in orders:
                #     print(f"{i[0]} \t {i[1]} \t {i[9]} \t {i[2]}  \t {i[3]} \t {i[4]} \t\t {i[5]} \t\t {i[6]} \t {i[7]} \t {i[8]} ")
        except Exception as e:
            print(e)

