import sqlite3, csv, os



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
                    itemid INTEGER,
                    itemname TEXT,
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
        except:
            print("Importing file failed. ")

    def view_menu(self):
        try:
            with con:
                cur.execute("SELECT * FROM menu")
                menu = cur.fetchall()
                print(f"{menu} \n\n  item id \t itemname \t  description ")
                for i in menu:
                    print(f"\t{i[0]} \t {i[1]} \t {i[2]}")
        except Exception:
            print("fel. kan inte vias meny ")

    def add_order(self):
        try:
            itemid = input("Enter item id: ")
            # cur.execute("SELECT menu.itemid FROM menu WHERE item = ?", itemid)
            # menuid_check = cur.fetchone()
            # if menuid_check != itemid:
            #     print("not a menu option ")
            #     self.add_order()
            # cur.execute("SELECT menu.itemname FROM menu, orders WHER itemid = itemid")
            extrasugar = input("Do you want extra sugar?(y/n) ")
            # if extrasugar != "y" or "N":
            #     self.add_order()
            extramilk = input("Do you want extra milk?(y/n) ")
            # if extrasugar != "y" or "N":
            #     self.add_order()
            with con:
                cur.execute(CREATE_TABLE_ORDERS)
                print("tabell skapad")
                cur.execute("SELECT * FROM menu")
                cur.execute(INSERT_DATA_ORDERS, (itemid, extrasugar, extramilk, "n"))
                print("order skapad")
        except Exception:
            print("error. kunte inte lägga till order. ")

    def show_orders(self):
        try:
            with con:
                #cur.execute("SELECT * FROM orders")
                cur.execute("SELECT * FROM orders WHERE completed = 'n'")
                print("letar i db \n")
                orders = cur.fetchall()
                print("orderid itemid itemname extrasugar extramilk completed timestamp")
                for i in orders:
                    print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]} \t\t {i[4]} \t {i[5]} \t {i[6]}")

        except Exception:
            print("error . kunde inte trycka order ")






    def delete_db(self):
        os.remove("devops22-python\shop.db")