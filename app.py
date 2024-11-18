from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "genAI":
            return "AI Generated!"  # Placeholder
        elif action == "End":
            return "Session Ended!"  # Placeholder
    return render_template("index.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        name = request.form.get("q")
        return render_template("main.html", name=name)
    return "Invalid Access"  # Optional

if __name__ == "__main__":
    app.run(port=5000)
