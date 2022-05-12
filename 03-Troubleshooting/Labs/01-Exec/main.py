import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    if os.env.get("USER"):
        return f"<p>Hello, {os.env['USER']}!</p>"
    else:
        return "<p>Hello, World!</p>"

