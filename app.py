from flask import Flask, render_template, request
from model import process_input

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    result = None

    if request.method == "POST":

        user_input = request.form["message"]

        words, emotion, response = process_input(user_input)

        result = {
            "input": user_input,
            "words": words,
            "emotion": emotion,
            "response": response
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)