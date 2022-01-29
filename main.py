from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"



@app.route("/")
def main():
    a = np.array([1, 2, 3, 4, 5, 6, 7])

    b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

    b = b.transpose()

    c = np.arange(0, 100, 1)


    d = np.linspace(0, 2, 10)


    e = np.arange(0, 100, 5)


    return render_template("widok.html", a=a, b=b, c=c, d=d, e=e)


if __name__ == "__main__":
    app.run(debug=True)