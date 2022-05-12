import sqlite3
def insert_teacher(teacher_name,phone_number,address,teacher_education):
    #Connecting to sqlite
    print("conecting to database")
    conn = sqlite3.connect('attendance_system_DB.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database.
    print("excuting sql query")
    cursor.execute('''INSERT INTO TEACHER(
       TEACHER_NAME,PHONE_NUMBER,ADDRESS,TEACHER_EDUCATION) VALUES 
       (\''''+teacher_name+'''\',\''''+phone_number+'''\',\''''+address+'''\',\''''+teacher_education+'''\')''')
    conn.commit()
    print("excuting query is done")
