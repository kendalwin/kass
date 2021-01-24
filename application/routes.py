from flask import render_template

from application import app


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/collegesearch")
def auditorium():
    return render_template("collegesearch.html")


@app.route("/explore")
def exhibits():
    return render_template("explore.html")

@app.route("/mycollege")
def photobooth():
    return render_template("mycollege.html")


@app.route("/scholarships")
def sponsors():
    return render_template("scholarships.html")

@app.route("/stats")
def about():
    return render_template("stats.html")

