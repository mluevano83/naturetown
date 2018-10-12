from flask import Flask, request, redirect, render_template, flash, url_for

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST', 'GET'])
def home_page():
        return render_template("index.html")

@app.route("/contact", methods=['POST', 'GET'])
def contact_page():
        return render_template("contact.html")

@app.route("/about", methods=['POST', 'GET'])
def about_page():
        return render_template("about.html")

@app.route("/posts", methods=['POST', 'GET'])
def posts_page():
        return render_template("posts.html")

if __name__ == '__main__':
    app.run()