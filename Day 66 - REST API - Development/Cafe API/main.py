import random

from flask import Flask, jsonify, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float, asc, desc, Boolean

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
# initialize the app with the extension
Bootstrap(app)
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def __repr__(self):
        return "<Cafe %r>" % self.name

    def to_dict(self):
        # Method 1.
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     # Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


# sample_cafe = Cafe(name="lk", map_url="/", img_url="/", location="null", seats="9", has_toilet=1, has_wifi=1,
#                    has_sockets=0, can_take_calls=1, coffee_price="5")


@app.route("/")
def home():
    # db.session.add(sample_cafe)
    # print("Committed")
    # db.session.commit()
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    data = Cafe.query.all()
    random_cafe = random.choice(data)
    # converting to Json
    data_json = jsonify(
        cafe={
            'name': random_cafe.name,
            'map_url': random_cafe.map_url,
            'img_url': random_cafe.img_url,
            'location': random_cafe.location,
            'amenities': {
                'seats': random_cafe.seats,
                'has_toilet': random_cafe.has_toilet,
                'has_wifi': random_cafe.has_wifi,
                'has_sockets': random_cafe.has_sockets,
                'can_take_calls': random_cafe.can_take_calls,
                'coffee_price': random_cafe.coffee_price,
            }
        }
    )
    # return rson

    # OR

    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def get_all_cafes():
    all_cafes = []
    data = Cafe.query.all()
    # This uses a List Comprehension but you could also split it into 3 lines.
    return jsonify(cafes=[cafe.to_dict() for cafe in data])


@app.route('/search')
def search():
    # a way of getting arguments
    location = request.args.get('loc')
    cafe = db.session.query(Cafe).filter_by(location=location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    # cafe_to_update = db.get_or_404(Cafe, int(cafe_id))
    cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the new price."}), 200
    else:
        return jsonify(response={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404


## HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def report_closed(cafe_id):
    api_key = request.args.get('api-key')
    if api_key == app.secret_key:
        cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from database."}), 200
        else:
            return jsonify(response={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(
            response={"error": "Sorry, that's not allowed. Make sure you have the correct the api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)

# To test our API, we can use ***Postman*** (https://www.postman.com/downloads/)
# It allows you to add key-value pairs for your request parameters and it will automatically format your URL
# It will also allow you to automatically create documentation for your API
