import sqlite3, csv

def create_table():
    CREATE_TABLE_PERSON = '''
                    CREATE TABLE IF NOT EXISTS mypersons(
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        firstname TEXT,
                        lastname TEXT,
                        birthdate TEXT,
                        adress TEXT,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                    )
                    '''

def insert_data():
    INSERT_DATA = '''
                INSERT INTO mypersons(
                    firstname,
                    lastname,
                    birthdate,
                    adress
                )
                VALUES (?, ?, ?, ?)
                '''

def open_csv():   
    file_path = "lesson_11/davidhasenson/person.csv" #input("Enter path to file: ")
    with open(file_path) as myfile:
        reader = csv.reader(myfile)
        for row in reader:
            print(row)



def create_table():
    with sqlite3.connect('mypersons.db', isolation_level=None) as conn:
        conn.execute(CREATE_TABLE_PERSON)
        
        
def insert_data():        
    with sqlite3.connect('mypersons.db', isolation_level=None) as conn:    
        conn.execute(INSERT_DATA, (?,?,?,?))

with sqlite3.


for person in conn.execute("SELECT * FROM mypersons"):
    print(person)

conn.close()

try:
    file_path = "lesson_11/davidhasenson/person.csv" #input("Enter file path: ")
    with open(file_path, "r") as f:
        print(f)
except FileNotFoundError:
    print("File not found")