from flask import Flask, render_template, request
import os

app = Flask(__name__)


# this route is for login page
@app.route('/')
def login():
    # render login.html page
    return render_template("login.html")


# this route is for signup page
@app.route('/signup')
def signup():
    # render signup.html page
    return render_template("signup.html")


# this route is for add_books page
@app.route('/add_books')
def add_books():
    # render add_books.html page
    return render_template("add_books.html")


# this route is for view_books page
@app.route('/view_books')
def view_books():
    from database import view_books
    books_dict = view_books()
    print(books_dict)
    # render view_books.html page
    return render_template("view_books.html", books_dict=books_dict)


# this route is for save_user page
@app.route('/API/save_user', methods=['post'])
def save_user():
    name = request.form.get('name')  # access the data inside
    username = request.form.get('username')
    password = request.form.get('password')
    type = request.form.get('type')
    print(name, username, password, type)
    from database import insert_user
    insert_user(name, username, password, type)
    # render signup.html page
    return render_template("signup.html")


# this route is for api/login page
@app.route('/API/login', methods=["post"])
def api_login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    print(password)
    from database import validate_user
    is_valid_user = validate_user(username, password)
    if is_valid_user == True:
        # render add_books.html page
        return render_template("add_books.html")
    # render login.html page
    return render_template("login.html")


# this route is for api/save_books page
@app.route('/API/save_books', methods=['post'])
def save_books():
    book_name = request.form.get('book_name')  # access the data inside
    author_name = request.form.get('author_name')
    book_price = request.form.get('book_price')

    print(book_name, author_name, book_price)
    from database import insert_books
    insert_books(book_name, author_name, book_price)
    # render add_books.html page
    return render_template("add_books.html")


if __name__ == '__main__':
    if 'PORT' in os.environ:
        port = os.environ['PORT']
    else:
        port = 5000
    app.run(debug=True, host="0.0.0.0", port=port)
