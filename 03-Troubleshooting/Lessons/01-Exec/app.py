import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    if os.getenv("USER"):
        return f"<p>Hello, {os.getenv['USER']}!</p>"
    else:
        return "<p>Hello, World!</p>"



if __name__ == "__main__":
    app.run(debug=True)
    