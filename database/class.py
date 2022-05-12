import sqlite3
def insert_class():
    #Connecting to sqlite
    conn = sqlite3.connect('../sqlite.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database.
    cursor.execute('''INSERT INTO CLASS(
       CLASS_NAME,ROOM_NUMBER,FLOOR_NUMBER) VALUES 
       ('COMPUTER CLASS', '9', '2')''')
