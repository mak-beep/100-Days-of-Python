from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# SQL COMMANDS

# For Database
# import sqlite3

# # Creating connection with database
# db = sqlite3.connect("books-collection.db")
# # to create a cursor which will control our database
# cursor = db.cursor()
# # Creating tables
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# # cursor.execute("CREATE TABLE BOOKS (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# Using SQLAlchemy
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# db = SQLAlchemy(app)


# Definition of your database models including the columns for the tables,
# which are named without an explicit definition based on the name of the
# respective model.


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


# Creation of the database tables within the application context.
with app.app_context():
    db.create_all()

    # print(Books.query.all())
# book1 = Books(title="Harry Potter", author="J.K Rowling", rating=9.0)
# with app.app_context():
    # db.session.add(book1)
with app.app_context():
    # Books.query.delete()
    # db.session.commit()
    all_books = Books.query.all()

    # # Getting all Records
    # # Update A Particular Record By Query
    # book = Books.query.filter_by(title='Harry Potter').first()
    # print(book)
    # # Update A Record By PRIMARY KEY
    # book = Books.query.get(1)
    # print(book)
    # # Delete A Particular Record By PRIMARY KEY
    # db.session.delete(book)
    #
    # db.session.commit()
    # # book.title = "Harry Potter and the Prisoner of Azkaban"
    # # db.session.commit()
    # print(Books.query.all())


@app.route('/')
def home():
    print(Books.query.all())
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        new_book = request.form.to_dict()
        book_ = Books(title=new_book.get('title'), author=new_book.get('author'), rating=new_book.get('rating'))
        print(Books.query.all())
        # with app.app_context():
        db.session.add(book_)
        # with app.app_context():
        db.session.commit()
        print(Books.query.all())

        # db.session.refresh(book)
        all_books.append(new_book)
        # print(new_book)
    return render_template('add.html')


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Books.query.get(book_id)
    print(book_id)
    return render_template("edit.html", book=book_selected)

if __name__ == "__main__":
    app.run(debug=True)
