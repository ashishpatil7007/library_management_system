import sqlite3
import pandas
def insert_student(student_name,phone_number,address,parent_phone_number):
    #Connecting to sqlite
    print("conecting to database")
    conn = sqlite3.connect('attendance_system_DB.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database
    print("excuting sql query")
    cursor.execute('''INSERT INTO STUDENT(
       STUDENT_NAME,PHONE_NUMBER,ADDRESS,PARENT_PHONE_NUMBER) VALUES 
       (\''''+student_name+'''\',\''''+phone_number+'''\',\''''+address+'''\',\''''+parent_phone_number+'''\')''')
    conn.commit()
    print("excuting query is done")

def view_student():
        # Connecting to sqlite
        print("conecting to database")
        conn = sqlite3.connect('attendance_system_DB.db')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        df = pandas.read_sql("select * from student", con=conn)
        print(df)
        conn.close()
        return df.to_dict("records")
