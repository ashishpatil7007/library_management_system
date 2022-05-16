import sqlite3
def insert_class(class_name,room_number,floor_number):
    #Connecting to sqlite
    print("conecting to database")
    conn = sqlite3.connect('attendance_system_DB.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database.
    print("excuting sql query")
    cursor.execute('''INSERT INTO CLASS(
       CLASS_NAME,ROOM_NUMBER,FLOOR_NUMBER) VALUES 
       (\''''+class_name+'''\',\''''+room_number+'''\',\''''+floor_number+'''\')''')
    conn.commit()
    print("excuting query is done")
