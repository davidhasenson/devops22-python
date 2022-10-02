from menu import *
from shoppingcart import *
import json
import sqlite3
import csv

#con = sqlite3.connect("articles.db")
#cur = con.cursor()

def load_file_json():
    path = "slutuppgift\items.json" #input("Enter path to file: ")
    with open(path) as f:
        items = json.load(f)
        #print(items)
        for item in items['items']:
            # Use this in executes second argument
            executeValues = tuple(item.values())
            print(executeValues)

def load_file_json_2():
    with open("slutuppgift\items.json") as f:
        data_to_database_executemany = []
        items = json.load(f)
        for item in items['items']:
            data_to_database_executemany.append(tuple(item.values()))
    print(data_to_database_executemany)
    
def import_csv_file():
    con = sqlite3.connect("articles.db")
    cur = con.cursor()
    path = "slutuppgift\items.csv" #input("Enter file path: ")
    with open(path, "r") as file:
        reader = csv.reader(file)
        with con:
            cur.execute(create_table_items())
            for row in reader:
                cur.execute(insert_data_into_items(), row)

def get_all_items():
    try:
        con = sqlite3.connect("articles.db")
        cur = con.cursor()
        with con:
            cur.execute("SELECT itemname, price FROM items ")
            all_items = cur.fetchall()
            print(all_items)
            for i in all_items:
                    print(f"{i[0]} ")
    except:
        print("Error. No data in database. ")
        
def get_all_items_with_price():
    try:
        con = sqlite3.connect("articles.db")
        cur = con.cursor()
        with con:
            cur.execute("SELECT itemname, price FROM items ")
            all_items = cur.fetchall()
            print(all_items)
            for i in all_items:
                    print(f"{i[0]} \t\t {i[1]}  ")
    except:
        print("Error. No data in database. ")

def create_table_items():
            return """
                    CREATE TABLE IF NOT EXISTS items(
                    itemname TEXT, 
                    price
                    )
                    """

def insert_data_into_items():
        return """
                INSERT INTO items(
                    itemname ,
                    price
                ) 
                VALUES (?, ?)
                """

def create_table_cart():
            return """
                    CREATE TABLE IF NOT EXISTS cart(
                    itemname TEXT, 
                    numberofitems
                    )
                    """

def add_item():
    try:
        item = input("Enter item to add: ")
        price = input("Enter price to add: ")
        con = sqlite3.connect("articles.db")
        cur = con.cursor()
        with con:
            cur.execute(insert_data(), (item, price,))   
    except:
        print("Error. can not add to db. ")      

def insert_data_into_cart():
    con = sqlite3.connect("articles.db")
    cur = con.cursor()
    item = input("enter item: ")
    amount = input("enter amount")
    with con:
        cur.execute("""
                    INSERT INTO cart(
                    itemname ,
                    numberofitems
                    ) 
                    VALUES (?, ?)
                    """, (item, amount,))


# def create_table_cart():
#     con = sqlite3.connect("articles.db")
#     cur = con.cursor()
#     with con:
#         cur.execute("""
#                     CREATE TABLE IF NOT EXISTS cart(
#                     itemname TEXT, 
#                     numberofitems
#                     )
#                     """)

def add_to_cart():
    try:
        item = input("Enter item to add: ")
        price = input("Enter price to add: ")
        con = sqlite3.connect("articles.db")
        cur = con.cursor()
        create_table_cart()
        with con:
            cur.execute(insert_data_into_cart(), (item, price,))   
    except:
        print("Error. can not add to cart. ")      



# CREATE_TABLE_ITEMS_2 = '''
#                 CREATE TABLE IF NOT EXISTS items(
#                     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                     itemname TEXT UNIQUE,
#                     price REAL,
#                     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
#                 )
#                 '''





def main():
    Menu().menu_loop()
    

if __name__ == "__main__":
    main()




----------------------------------------------------------------------------------





from menu import *
from shoppingcart import *
import json
import sqlite3
import csv

#con = sqlite3.connect("articles.db")
#cur = con.cursor()

def load_file_json():
    path = "slutuppgift\items.json" #input("Enter path to file: ")
    with open(path) as f:
        items = json.load(f)
        #print(items)
        for item in items['items']:
            # Use this in executes second argument
            executeValues = tuple(item.values())
            print(executeValues)

def load_file_json_2():
    with open("slutuppgift\items.json") as f:
        data_to_database_executemany = []
        items = json.load(f)
        for item in items['items']:
            data_to_database_executemany.append(tuple(item.values()))
    print(data_to_database_executemany)
    
def import_csv_file():
    con = sqlite3.connect("articles.db")
    cur = con.cursor()
    path = "slutuppgift\items.csv" #input("Enter file path: ")
    with open(path, "r") as file:
        reader = csv.reader(file)
        with con:
            cur.execute(create_table_items())
            for row in reader:
                cur.execute(insert_data_into_items(), row)

def get_all_items():
    try:
        con = sqlite3.connect("articles.db")
        cur = con.cursor()
        with con:
            cur.execute("SELECT itemname, price FROM items ")
            all_items = cur.fetchall()
            print(all_items)
            for i in all_items:
                    print(f"{i[0]} ")
    except:
        print("Error. No data in database. ")
        
def get_all_items_with_price():
    try:
        con = sqlite3.connect("articles.db")
        cur = con.cursor()
        with con:
            cur.execute("SELECT itemname, price FROM items ")
            all_items = cur.fetchall()
            print(all_items)
            for i in all_items:
                    print(f"{i[0]} \t\t {i[1]}  ")
    except:
        print("Error. No data in database. ")

def create_table_items():
            return """
                    CREATE TABLE IF NOT EXISTS items(
                    itemname TEXT, 
                    price
                    )
                    """

def insert_data_into_items():
        return """
                INSERT INTO items(
                    itemname ,
                    price
                ) 
                VALUES (?, ?)
                """

def add_item():
    try:
        item = input("Enter item to add: ")
        price = input("Enter price to add: ")
        con = sqlite3.connect("articles.db")
        cur = con.cursor()
        with con:
            cur.execute(insert_data_into_items(), (item, price,))   
    except:
        print("Error. can not add to db. ")      

def create_table_cart():
            return """
                    CREATE TABLE IF NOT EXISTS cart(
                    itemname TEXT, 
                    numberofitems
                    )
                    """ 

def insert_data_into_cart():
            return """
                    INSERT INTO cart(
                    itemname ,
                    numberofitems
                    ) 
                    VALUES (?, ?)
                    """
def create_table_cart():
    con = sqlite3.connect("articles.db")
    cur = con.cursor()
    try:
        with con:
            create_table_cart()
    except:
        print("error. No cart table created. ")

def add_to_cart():
    try:
        item = input("Enter item to add to cart: ")
        amount = input("Enter amount to add: ")
        con = sqlite3.connect("articles.db")
        with con:
            cur.execute(insert_data_into_cart(), (item, amount,))   
    except:
        print("Error. can not add to cart. ")      

def main():
    Menu().menu_loop()
    
if __name__ == "__main__":
    main()


# CREATE_TABLE_ITEMS_2 = '''
#                 CREATE TABLE IF NOT EXISTS items(
#                     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                     itemname TEXT UNIQUE,
#                     price REAL,
#                     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
#                 )
#                 '''