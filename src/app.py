#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return """
    <h2>Select Language</h2>
    <form action="/greet" method="POST">
        <label>
            <input type="radio" name="language" value="en" required>
            English
        </label><br>
        <label>
            <input type="radio" name="language" value="de">
            Deutsch
        </label><br><br>

        <label>Your Name:</label><br>
        <input name="name" required><br><br>

        <input type="submit" value="Submit">
    </form>
    """

@app.route("/greet", methods=["POST"])
def greet():
    language = request.form.get("language")
    name = request.form.get("name", "")

    if language == "en":
        greeting = "Good day"
    elif language == "de":
        greeting = "Guten Tag"
    else:
        greeting = "Hello"

    return f"{greeting}, {name}!"

