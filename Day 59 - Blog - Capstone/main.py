from flask import Flask, render_template
import requests
from post import Post

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


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<index>')
def show_post(index):
    try:
        target_post = blog_posts[int(index)-1]
    except IndexError:
        return f"<h1>Error 404</h1>"
    else:
        post = Post(target_post)
        return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
