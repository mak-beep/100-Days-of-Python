from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float, asc, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os

load_dotenv()

MOVIE_DB_API_KEY = os.environ.get("API_KEY")
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie/"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500/"
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
# initialize the app with the extension
Bootstrap(app)
db = SQLAlchemy(app)


class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float, default=0)
    ranking: Mapped[int] = mapped_column(Integer, default=0)
    review: Mapped[str] = mapped_column(String, default="")
    img_url: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return "<Movie %r>" % self.title


class updateMovie(FlaskForm):
    rating = StringField('Your Rating out of 10 e.g., 7.6', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField("Done")


class addMovie(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField("Add Movie")


with app.app_context():
    db.create_all()
    all_books = Movies.query.all()
# for website use
# all_movies = None

# new_movie = Movies(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

with app.app_context():
    db.create_all()
    all_movies = Movies.query.all()


@app.route("/", methods=['POST', 'GET'])
def home():
    global all_movies
    if request.method == 'POST':
        data = request.form.to_dict()
        movie_to_edit = db.get_or_404(Movies, int(data['id']))
        movie_to_edit.rating = data['rating']
        movie_to_edit.review = data['review']
        db.session.commit()

    # all_movies = Movies.query.all()
    # Descending Order
    # all_movies = Movies.query.order_by(desc(Movies.rating)).all()
    # Ascending Order
    all_movies = Movies.query.order_by(Movies.rating).all()
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    # q = db.session.query(Movies)
    db.session.commit()
    print(all_movies)
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        data = request.form.to_dict()
        movie_title = data['title']
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    else:
        form = addMovie()
        return render_template("add.html", form=form)


@app.route("/edit/<index>")
def edit(index):
    movie_form = updateMovie()
    movie_to_update = db.get_or_404(Movies, int(index))
    return render_template("edit.html", movie=movie_to_update, form=movie_form)


@app.route("/delete/<index>")
def delete(index):
    movie_to_delete = db.get_or_404(Movies, int(index))
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/find/<index>")
def find(index):
    movie_api_id = index
    # print(movie_api_id)
    if movie_api_id:
        movie_form = updateMovie()
        movie_api_url = f"{MOVIE_DB_INFO_URL}{movie_api_id}"
        # print(movie_api_url)
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        # print(data)
        new_movie = Movies(
            title=data["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )

        db.session.add(new_movie)
        print(new_movie.rating)
        db.session.commit()

        return render_template('edit.html', movie=new_movie, form=movie_form)


if __name__ == '__main__':
    app.run(debug=True)
