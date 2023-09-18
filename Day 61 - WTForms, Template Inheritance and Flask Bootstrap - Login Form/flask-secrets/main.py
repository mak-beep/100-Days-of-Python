from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# For adding Bootstrap to our app
from flask_bootstrap import Bootstrap

# Login Credentials [Dummy]
LOGIN_email= "admin@email.com"
LOGIN_password= "12345678"

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Provide correct email.')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password must be at least 8 characters long.')])
    submit = SubmitField("Log in")


app = Flask(__name__)
app.secret_key = "day61_of_100"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET","POST"])
def login():
    login_form = LoginForm()
    # if validation was successful after the user submitted the form
    if login_form.validate_on_submit():
        if (LOGIN_email == login_form.email.data) and (LOGIN_password == login_form.password.data):
            print("Logged In")
            return render_template('success.html')
        else:
            print("Incorrect Credentials.\nTry Again.")
            return render_template('denied.html')

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)