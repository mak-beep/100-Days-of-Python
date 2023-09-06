from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests
app = Flask(__name__)


@app.route('/')
def home():
    random_number = randint(1,10)
    current_year = datetime.now().year
    return render_template("index.html",num=random_number, copyright_year=current_year)


@app.route('/guess/<name>')
def guess_gender(name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    nationality_response = requests.get(url=f"https://api.nationalize.io?name={name}")
    age = age_response.json()['age']
    nationality = nationality_response.json()['country'][0]['country_id']

    gender = gender_response.json()['gender']
    return render_template("guess.html", name=name, gender=gender, age=age, nationality=nationality)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/07978e257b3756696de5'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog_post.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


