from flask import Flask, render_template, request
import requests
from post import Post
import os
import smtplib

OWN_EMAIL = os.environ.get("MY_EMAIL")
OWN_PASSWORD = os.environ.get("MY_PASSWORD")

GMAIL_HOST = "smtp.gmail.com"


app = Flask(__name__)

blog_api = "https://api.npoint.io/68240898889ef7cae926"

response = requests.get(url=blog_api)
blog_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        # print(data['name'])
        # print(data['email'])
        # print(data['phone'])
        # print(data['message'])
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", sent_data=True)
    else:
        return render_template("contact.html", sent_data=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        # We are actually sending email to us from our own account, with the form data
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

@app.route('/post/<index>')
def show_post(index):
    try:
        target_post = blog_posts[int(index) - 1]
    except IndexError:
        return f"<h1>Error 404</h1>"
    else:
        post = Post(target_post)
        return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
