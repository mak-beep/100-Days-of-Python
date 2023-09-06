import requests
from flask import Flask, render_template
from post import Post

app = Flask(__name__)
blog_api = 'https://api.npoint.io/07978e257b3756696de5'
response = requests.get(blog_api)
all_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", blog_posts=all_posts)

@app.route('/posts/<index>')
def show_post(index):
    try:
        target_post = all_posts[int(index)-1]
    except IndexError:
        return f"<h1>Error 404</h1>"
    else:
        post = Post(target_post)
        return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
