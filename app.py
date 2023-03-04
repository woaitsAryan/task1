from flask import Flask, redirect, url_for, request, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("basic.html")

@app.route("/calculate", methods = ['POST'])
def calculate():
    x = int(request.form.get('x'))
    y = int(request.form.get('y'))
    operation = request.form.get('operation')
    if operation == "add":
        return redirect(url_for('add', x = x, y = y))
    elif operation == "subtract":
        return redirect(url_for('subtract', x = x, y = y))
    else:
        return redirect(url_for('multiply', x = x, y = y))

@app.route("/<int:x>+<int:y>")
def add(x,y):
    answer = requests.get(f"http://127.0.0.1:8080/{x}+{y}")
    if answer.status_code == 200:
        return render_template("succcess.html", answer = answer.json())
    else:
        return render_template("success.html", answer = answer.status_code)


@app.route("/<int:x>-<int:y>")
def subtract(x,y):
    answer = requests.get(f"http://127.0.0.1:8080/{x}-{y}")
    if answer.status_code == 200:
        return render_template("success.html", answer = answer.json())
    else:
        return render_template("success.html", answer = answer.status_code)

app.route("/<int:x>*<int:y>")
def multiply(x,y):
    answer = requests.get(f"http://127.0.0.1:8081/{x}*{y}")
    if answer.status_code == 200:
        return render_template("success.html", answer = answer.json())
    else:
        return render_template("success.html", answer = answer.status_code)