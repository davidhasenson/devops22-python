import json
import sqlite3

class Dbhandler:

    def __init__(self):
        pass

    CREATE_TABLE_ITEMS = '''
                CREATE TABLE IF NOT EXISTS items(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    itemname TEXT UNIQUE,
                    price REAL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                )
                '''

    INSERT_DATA = '''
            INSERT INTO item(
                itemname,
                price
            )
            VALUES (?, ?)
            '''



