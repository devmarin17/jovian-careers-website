# Flask import
from flask import Flask, render_template

# Creating App
app = Flask(__name__)


# Creating route (home page)
@app.route("/")
def home():
  return render_template("home.html")


# Run flask with run app.py
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
