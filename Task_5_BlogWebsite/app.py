from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

POSTS_FILE = "posts.json"

# Load posts from file
def load_posts():
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, "r") as f:
            return json.load(f)
    return []

# Save posts to file
def save_posts(posts):
    with open(POSTS_FILE, "w") as f:
        json.dump(posts, f, indent=4)

@app.route("/")
def index():
    posts = load_posts()
    posts.reverse()  # latest post first
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def view_post(post_id):
    posts = load_posts()
    if 0 <= post_id < len(posts):
        return render_template("post.html", post=posts[post_id])
    return "Post not found", 404

@app.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        posts = load_posts()
        new_post = {
            "title": request.form["title"],
            "content": request.form["content"],
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "image_url": request.form.get("image_url", ""),
            "video_url": request.form.get("video_url", "")
        }
        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for("index"))
    return render_template("add_post.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
