#syn code spaces is very high risk, sometimes fail
#hello
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "PUT"])
def index():
    return render_template("index.html")

@app.route("/main", methods=["GET", "PUT"])
def main():
    name = request.form.get("q")
    return render_template("main.html")


if __name__ == "__main__":
    app.run(port=1111)
