import requests
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

response = requests.get("https://jsonplaceholder.typicode.com/users?_limit=6")
posts_list = response.json()

@app.route("/")
def index():
    return render_template("index.html", users=posts_list)

@app.route("/remove/<int:user_id>", methods=["POST"])
def remove_user(user_id):
    requests.delete(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    
    global posts_list
    posts_list = [u for u in posts_list if u['id'] != user_id]
    
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)