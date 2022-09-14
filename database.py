import sqlite3
import pandas
def insert_user(name,username,password,type):
    #Connecting to sqlite
    print("conecting to database")
    conn = sqlite3.connect('library_management_system_DB.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database
    print("excuting sql query")
    cursor.execute('''INSERT INTO USER(
       NAME,USER_NAME,PASSSWORD,USER_TYPE) VALUES 
       (\''''+name+'''\',\''''+username+'''\',\''''+password+'''\',\''''+type+'''\')''')
    conn.commit()
    print("excuting query is done")
def validate_user(username,password):
    # Connecting to sqlite
    conn = sqlite3.connect('library_management_system_DB.db')

    # Creating a cursor object using the
    # cursor() method
    cursor = conn.cursor()
    df= pandas.read_sql(f'''select * from USER where USER_NAME='{username}' and PASSSWORD='{password}' '''.format(username=username,password=password),conn)
    print(df)

    if df.empty:
        return False
    else:
        return True

def insert_books(book_name,author_name,book_price):
    #Connecting to sqlite
    print("conecting to database")
    conn = sqlite3.connect('library_management_system_DB.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database
    print("excuting sql query")
    cursor.execute('''INSERT INTO BOOKS(
       BOOK_NAME,AUTHOR_NAME,PRICE) VALUES 
       (\''''+book_name+'''\',\''''+author_name+'''\',\''''+book_price+'''\')''')
    conn.commit()
    print("excuting query is done")

def view_books():
        # Connecting to sqlite
        print("conecting to database")
        conn = sqlite3.connect('library_management_system_DB.db')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        df = pandas.read_sql("select * from BOOKS", con=conn)
        print(df)
        conn.close()
        return df.to_dict("records")

