from flask import Flask, render_template
import requests
import post as p

app = Flask(__name__)

@app.route('/')
def home():
    blog_posts = blogs()
    return render_template("index.html", blog_posts=blog_posts)


def blogs():
    print()
    blog_url = "https://api.npoint.io/4d1edc5c503fdb1b30a3"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return all_posts


@app.route("/post/<int:blog_num>")
def get_blog(blog_num):
    post = p.Post(blog_id=blog_num)
    return render_template("post.html", blog_post=post.post)

if __name__ == "__main__":
    app.run(debug=True)
