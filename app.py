from flask import Flask, render_template, request, session
import textblob
import google.generativeai as genai
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

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
            session.pop('conversation', None)  # Clear the conversation history
            return "Session Ended!"  # Placeholder
    return render_template("index.html")

@app.route("/generate_ai_result", methods=["GET", "POST"])
def generate_ai_result():
    if 'conversation' not in session:
        session['conversation'] = []

    if request.method == "POST":
        question = request.form.get("question")
        r = model.generate_content(question)
        generated_code = r.candidates[0].content.parts[0].text

        # Append the question and response to the conversation history
        session['conversation'].append({'question': question, 'response': generated_code})

        # Keep only the last 20 conversations
        if len(session['conversation']) > 20:
            session['conversation'] = session['conversation'][-20:]

    return render_template("generate_ai.html", conversation=session['conversation'])

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