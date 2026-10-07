from flask import Flask

app = Flask(__name__)

# ---------- Routes ----------
@app.route("/")
def hello_world():
  return "<p>Homepage!</p>"

@app.route("/projects")
def projects():
  return "<p>Projects page</p>"

@app.route("/about")
def about():
  return "<p>About page</p>"

