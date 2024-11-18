#syn code spaces is very high risk, sometimes fail
#hello
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    name = request.form.get("q")  # Ensure 'q' matches the name attribute in your form
    return render_template("main.html", name=name)

if __name__ == "__main__":
    app.run(port=1111)
