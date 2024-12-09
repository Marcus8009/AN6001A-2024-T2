from flask import Flask, render_template, request
import textblob
import google.generativeai as genai
import pandas as pd
import os 


app = Flask(__name__)

# Configure the generative AI model
api = os.getenv("MASKERSUITE")
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "genAI":
            return render_template("generate_ai.html")
        elif action == "End":
            return "Session Ended!"  # Placeholder
    return render_template("index.html")

@app.route("/generate_ai_result", methods=["POST"])
def generate_ai_result():
    question = request.form.get("question")
    r = model.generate_content(question)
    generated_code = r.candidates[0].content.parts[0].text
    return render_template("ai_result.html", generated_code=generated_code)

@app.route("/main", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        name = request.form.get("q")
        return render_template("main.html")
    return "Invalid Access"  # Optional

@app.route("/SA", methods=["GET", "POST"])
def SA():
    return render_template("SA.html")

@app.route("/SA_result", methods=["GET", "POST"])
def SA_result():
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    return render_template("SA_result.html", r=r)

if __name__ == "__main__":
    app.run(port=5000)