from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)

user_list = []


@app.route('/')
def index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
