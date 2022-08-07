import sqlite3
def insert_user(username,password):
    #Connecting to sqlite
    print("conecting to database")
    conn = sqlite3.connect('attendance_system_DB.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database
    print("excuting sql query")
    cursor.execute('''INSERT INTO USER(
       USER_NAME,PASSWORD) VALUES 
       (\''''+username+'''\',\''''+password+'''\')''')
    conn.commit()
    print("excuting query is done")
