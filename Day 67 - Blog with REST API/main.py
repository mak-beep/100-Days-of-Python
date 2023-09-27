from datetime import date

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()
    posts = BlogPost.query.all()


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    global posts
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = db.get_or_404(BlogPost, index)
    return render_template("post.html", post=requested_post)

@app.route('/new_post', methods=['GET','POST'])
def add_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)

@app.route('/edit_post', methods=['GET', 'POST'])
def edit_post():
    post_id = request.args.get('post_id')
    post_to_edit = db.get_or_404(BlogPost, int(post_id))
    # edit_form = CreatePostForm(
    #     title=post_to_edit.title,
    #     subtitle=post_to_edit.subtitle,
    #     img_url=post_to_edit.img_url,
    #     author=post_to_edit.author,
    #     body=post_to_edit.body,
    # )
    edit_form = CreatePostForm(obj=post_to_edit)
    if edit_form.validate_on_submit():
        post_to_edit.title = edit_form.title.data
        post_to_edit.subtitle = edit_form.subtitle.data
        post_to_edit.img_url = edit_form.img_url.data
        post_to_edit.author = edit_form.author.data
        post_to_edit.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", index=post_to_edit.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)

@app.route('/delete')
def delete_post():
    post_id = request.args.get('post_id')
    post_to_delete = db.get_or_404(BlogPost, int(post_id))
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect('/')


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)