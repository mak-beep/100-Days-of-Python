from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float)

    def __repr__(self):
        return "<Book >"


with app.app_context():
    db.create_all()
    all_books = Books.query.all()


@app.route('/', methods=['POST', 'GET'])
def home():
    global all_books
    if request.method == 'POST':
        data = request.form
        book_target = db.get_or_404(Books, data['id'])
        book_target.rating = data['rating']
        db.session.commit()
        all_books = Books.query.all()

    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        data = request.form.to_dict()
        new_book = Books(title=data['title'], author=data['author'], rating=data['rating'])
        db.session.add(new_book)
        db.session.commit()
        all_books.append(data)
    return render_template('add.html')


@app.route('/edit/<index>')
def edit(index):
    book_to_edit = db.get_or_404(Books, int(index))
    # print(book_to_edit)
    return render_template('edit.html', book=book_to_edit)


@app.route('/delete/<index>')
def delete(index):
    global all_books
    book_to_delete = db.get_or_404(Books, int(index))
    db.session.delete(book_to_delete)
    db.session.commit()
    all_books = Books.query.all()
    print(all_books)
    return redirect(url_for('home', book=all_books))


if __name__ == "__main__":
    app.run(debug=True)
