from app import app
from flask import render_template, request

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/particles.json")
def send_particles_json():
    return app.send_static_file('particles.json')
