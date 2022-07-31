from flask import *

app = Flask(__name__)


@app.route("/")
def hello_world(name=None):
    return render_template('hello.html', name=name)


@app.route("/username/<name>")
def greet(name):
    return f"Hello there, {name}"


if __name__ == "__main__":
    app.run(debug=True)
