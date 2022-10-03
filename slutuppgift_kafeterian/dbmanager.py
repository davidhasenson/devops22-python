from itertools import count
from operator import itemgetter
import sqlite3, csv, os, random
from ssl import Options
from menu import *


con = sqlite3.connect("slutuppgift_kafeterian\shop.db")
cur = con.cursor()


CREATE_TABLE_MENUITEMS = """
                CREATE TABLE IF NOT EXISTS menu(
                    itemid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    itemname TEXT UNIQUE,
                    description TEXT
                )
                """

INSERT_DATA_MENUITEMS = """
                INSERT INTO menu(
                    itemname,
                    description
                ) 
                VALUES (?, ?)
                """

CREATE_TABLE_ORDERS = """
                CREATE TABLE IF NOT EXISTS orders(
                    orderid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    itemid INTEGER NOT NULL,
                    extrasugar TEXT,
                    extramilk TEXT,
                    completed TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                )
                """

INSERT_DATA_ORDERS = """
                INSERT INTO orders(
                    itemid,
                    extrasugar,
                    extramilk,
                    completed
                ) 
                VALUES (?, ?, ?, ?)
                """

class Dbmanager:

    def __init__(self) -> None:
        pass

    # def create_table_menuitems(self):
    #         return '''
    #             CREATE TABLE IF NOT EXISTS person(
    #                 id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #                 itemname TEXT,
    #                 description TEXT,
    #             )
    #             '''

    # def insert_data_into_items(self):
    #     return """
    #             INSERT INTO items(
    #                 itemname,
    #                 price 
    #             ) 
    #             VALUES (?, ?)
    #             """
                
    def import_csv_file_to_db(self):
        try:   
            path = "slutuppgift_kafeterian\drycker.csv" #input("Enter file path: ")
            with open(path, "r") as file:
                reader = csv.reader(file)
                print(reader)
                with con:
                    cur.execute(CREATE_TABLE_MENUITEMS)
                    for row in reader:
                        print(row)
                        cur.execute(INSERT_DATA_MENUITEMS, row)
        except Exception:
            print("Importing file failed. ")

    def view_menu(self):
        try:
            with con:
                cur.execute("SELECT * FROM menu")
                menu = cur.fetchall()
                print(f"{menu} \n\n  Item id \t Item name \t Description ")
                for i in menu:
                    print(f"\t{i[0]} \t {i[1]} \t {i[2]}")
        except Exception:
            print("fel. kan inte vias meny ")

    def add_order(self):
        try:
            itemid = self.check_itemid("Enter item id to select beverage (0 to exit): ")
            print(itemid)
            if itemid == 0: # avoid infinite loop if menu empty.
                return
            extrasugar = self.input_y_or_n("Do you want extra sugar?(y/n) ")
            extramilk = self.input_y_or_n("Do you want extra milk?(y/n) ")
            with con:
                cur.execute(CREATE_TABLE_ORDERS)
                print("tabell skapad")
                cur.execute("SELECT * FROM menu")
                cur.execute(INSERT_DATA_ORDERS, (itemid, extrasugar, extramilk, "n"))
                print("order skapad")
        except Exception:
            print("Error. Could not complete order. ")

    def show_orders(self):
        try:
            with con:
                cur.execute("SELECT orders.*, menu.itemname FROM orders JOIN menu ON menu.itemid = orders.itemid WHERE completed = 'n'")
                print("letar i db \n")
                orders = cur.fetchall()
                print(f"{orders} \n")
                print("orderid  itemid  itemname  extrasugar extramilk completed timestamp")
                for i in orders:
                    print(f"{i[0]} \t {i[1]} \t {i[6]} \t {i[2]} \t {i[3]} \t {i[4]} \t  {i[5]} ")
        except Exception as e:
            print(e)

    def input_int(self, text):
        while True:
            try:
                input_test = int(input(text))
                print(input_test)
                return input_test
            except ValueError as v:
                print(v)
                print("måste ange en int")
            except Exception as e:
                print(e)

    def input_y_or_n(self,text):
            while True:
                try:
                    input_test = input(text).lower()
                    if input_test in  ("y", "n"):
                        return input_test
                    print("inte ett val. måste ange yes(y) or no(n)")
                except Exception as e:
                    print(e)    

    def check_itemid(self, text):
        while True:
            try:
                itemid = self.input_int(text)
                #print(f"itemid {itemid} ")
                cur.execute("SELECT menu.itemid FROM menu WHERE itemid = ?", (itemid,))
                menuid_check = cur.fetchone()
                #print(menuid_check)
                if menuid_check or itemid == 0:     # 0 to escape loop.
                    return itemid                   # Must be itemid to return 0.
                else:
                    print("Inte ett menyval ")
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
                print("not a menu option ")
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
                print("not a menu option ")
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
                    print("inte ett order id ")
                    continue
            except Exception as e:
                print(e)

    def complete_order(self):
        try:
            orderid = self.check_orderid("ange order id fär att slutdöra order. 0 to exit ")
            if orderid == 0:
                return
            cur.execute("UPDATE orders SET completed = 'y' WHERE orderid = ?", (orderid,))       #https://www.w3schools.com/sql/sql_update.asp
        except Exception as e:
            print(e)
       
    def delete_order(self):
        try:
            orderid = self.check_orderid("ange order id för borttagning. 0 to exit ")
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
                print(count)
                if not count:
                    print("tom meny")
                    return
                itemid = random.randint(1, count)
                print(itemid)
                extrasugar = random.choice(["y", "n"])
                extramilk = random.choice(["y", "n"])
                cur.execute(CREATE_TABLE_ORDERS)
                print("tabell skapad")
                cur.execute("SELECT * FROM menu")
                cur.execute(INSERT_DATA_ORDERS, (itemid, extrasugar, extramilk, "n"))
                print("order skapad")
        except Exception:
            print("Error. Could not complete order. ")

    def show_all_orders(self):
            try:
                with con:
                    cur.execute("SELECT orders.*, menu.itemname FROM orders JOIN menu ON menu.itemid = orders.itemid")
                    orders = cur.fetchall()
                    print("orderid  itemid  itemname  extrasugar extramilk completed timestamp")
                    for i in orders:
                        print(f"{i[0]} \t {i[1]} \t {i[6]} \t {i[2]} \t {i[3]} \t {i[4]} \t  {i[5]} ")
            except Exception as e:
                print(e)

    def show_completed_orders(self):
        try:
            with con:
                cur.execute("SELECT orders.*, menu.itemname FROM orders JOIN menu ON menu.itemid = orders.itemid WHERE completed = 'y'")
                orders = cur.fetchall()
                print("orderid  itemid  itemname  extrasugar extramilk completed timestamp")
                for i in orders:
                    print(f"{i[0]} \t {i[1]} \t {i[6]} \t {i[2]} \t {i[3]} \t {i[4]} \t  {i[5]} ")
        except Exception as e:
            print(e)



