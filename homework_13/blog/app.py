import sqlite3

from flask import Flask, render_template, request, redirect , url_for
import sqlite3

def get_db_connection():
    database = sqlite3.connect("database.db")
    database.row_factory = sqlite3.Row
    return database

def get_post(id):
    database = get_db_connection()
    post = database.execute("SELECT * FROM posts WHERE id = ?", (id,)).fetchone()
    return post

app = Flask(__name__)

@app.route('/') #дописывает доп страницу
def index():
    database = get_db_connection()
    posts = database.execute("SELECT * FROM posts ORDER BY posts.created DESC").fetchall()
    return render_template("index.html", posts=posts)



@app.route('/create/', methods=["GET","POST"])
def create():
    if request.method == "GET":
        return render_template("newPost.html")

    elif request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        content = request.form["content"]

        database = get_db_connection()
        database.execute("INSERT INTO posts (author, title, content) VALUES (?,?,?)", (author, title, content))

        database.commit()
        database.close()

        return redirect(url_for("index"))

@app.route('/about/', methods=["GET","POST"])
def about():
    if request.method == "GET":
        return render_template("about.html")



@app.route("/post-<int:id>/")
def post(id):
    post = get_post(id)
    return render_template("postDetail.html", post=post)

@app.route("/delete/post-<int:id>/", methods=["POST"])
def delete_post(id):
    database = get_db_connection()
    delete = database.execute("DELETE FROM posts WHERE id = ?",(id, )).fetchone()
    database.commit()
    database.close()
    return redirect(url_for('index'))

@app.route("/delete_all_posts/", methods=["POST"])
def delete_all_posts():
    database = get_db_connection()
    delete = database.execute("DELETE FROM posts")
    database.commit()
    database.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.config["TIMEZONE"] = "utc-2"
    app.run(debug=True)
