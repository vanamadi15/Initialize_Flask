from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome_page():
  return "Welcome to python's flask"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)