from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    URL = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(URL)
    blog_data = response.json()
    return render_template("index.html", blog_data = blog_data)

@app.route('/post/<int:post_id>')
def post(post_id):
    URL = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(URL)
    blog_data = response.json()
    post = next((item for item in blog_data if item["id"] == post_id), None)
    return render_template("post.html", post = post)

if __name__ == "__main__":
    app.run(debug=True)
