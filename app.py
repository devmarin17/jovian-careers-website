# Flask import
from flask import Flask

# Creating App
app = Flask(__name__)


# Creating route (home page)
@app.route("/")
def home():
  return "<p1>Hello, you!</p1>"


# Run flask with run app.py
if __name__ == "__main__":
  app.run(debug=True)
