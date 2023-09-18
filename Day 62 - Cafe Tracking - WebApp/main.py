from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import pandas

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Map (URL)', validators=[DataRequired(), URL(message='Invalid URL')])
    opening_time = StringField('Opening Time e.g., 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g., 5:30PM', validators=[DataRequired()])
    rating = SelectField('Coffee Rating', choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'), ('☕️☕️☕️', '☕️☕️☕️'), ('☕️☕️☕️☕️', '☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')], validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=[('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪️', '💪💪💪️'), ('💪💪💪💪', '💪💪💪💪️'), ('💪💪💪💪💪', '💪💪💪💪💪')], validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=[('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # print(csv)
        # form_data = dict()
        form_data = {key:[value] for (key,value) in form.data.items()}
        form_data = dict(list(form_data.items())[:7])
        print(form_data)
        new_data = pandas.DataFrame(data=form_data)
        new_data.to_csv("cafe-data.csv", mode='a', index=False, header=False)
        # print(form.data)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():

    csv_data = pandas.read_csv('cafe-data.csv')
    csv_file = csv_data.to_dict()
    keys_ = csv_data.keys()
    total_items = len(csv_data[keys_[0]])
    return render_template('cafes.html', cafes=csv_file, total_items=total_items)


if __name__ == '__main__':
    app.run(debug=True)
