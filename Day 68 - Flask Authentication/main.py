from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB.
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User,int(user_id))


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        data = request.form

        if User.query.filter_by(email=data['email']).first():
            flash("You have already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salt_password = generate_password_hash(
            password=data['password'],
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User()
        new_user.email = data['email']
        new_user.name = data['name']
        new_user.password = hash_and_salt_password
        db.session.add(new_user)
        db.session.commit()
        # Log in and authenticate user after adding details to database.
        login_user(new_user)
        user_data = User.query.all()

        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        data = request.form
        entered_email = data['email']
        entered_password = data['password']

        # Find user by email entered.
        user = User.query.filter_by(email=entered_email).first()
        if user:
            # Check stored password hash against entered password hashed.
            if check_password_hash(user.password, entered_password):
                login_user(user)
                flash('You were successfully logged in')
                return redirect(url_for('secrets'))
            else:
                flash('Password incorrect. Please try again.')

        else:
            flash("This Email doesn't exist. Please try again.")
    return render_template('login.html', logged_in=current_user.is_authenticated)


@app.route('/secrets')
# makes sure that, dont open '/secrets' if not logged in
@login_required
def secrets():
    # print(current_user.name)
    return render_template("secrets.html", logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("index.html")


@app.route('/download')
@login_required
def download():
    # add 'as_attachment=True' in parameters, to download automatically
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
