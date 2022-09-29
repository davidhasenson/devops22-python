from menu import *
from shoppingcart import Shoppingcart
import json
import sqlite3


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
    


CREATE_TABLE_ITEMS = '''
                CREATE TABLE IF NOT EXISTS items(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    itemname TEXT UNIQUE,
                    price REAL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                )
                '''

# con = sqlite3.connect("items.db")
# cur = con.cursor()

# cur.execute(CREATE_TABLE_ITEMS)




def main():
    #Menu().menu_loop()
    con = sqlite3.connect("items.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS items(itemname , price)")

    cur.execute("""
        INSERT INTO items VALUES
            ("banana", 5),
            ("apple", 7)
        """)
    con.commit()
    res = cur.execute("SELECT itemname FROM items")
    print(res.fetchall())
    cur.executemany("INSERT INTO items VALUES (?, ?)", load_file_json_2())

if __name__ == "__main__":
    main()

