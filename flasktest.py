from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landingpage():
    return render_template("landingpage.html")
@app.route("/anotherpage")
def anotherpage():
    return render_template("anotherpage.html")

if __name__ == "__main__":
    app.run(debug=True)