from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/main")
def index():
    return render_template("base.html")


@app.route("/classification")
def classification():
    return render_template("classification.html")


if __name__ == "__main__":
    app.run(debug=True)