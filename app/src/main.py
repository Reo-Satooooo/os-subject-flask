import os
from flask import Flask, render_template
from jinja2 import FileSystemLoader

app = Flask(__name__)
app.jinja_loader = FileSystemLoader(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../view'))

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()