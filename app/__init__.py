import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About Me",
        work_experiences=[
            {
                "position": "Production Engineer Fellow",
                "company": "Major League Hacking",
                "years": "2025–2025",
                "description": "Deployed a personal flask web application",
            },
            {
                "position": "Manager",
                "company": "Epic Theatres",
                "years": "2019-2020",
                "description": "Managed theatre operations",
            },
        ],
        education=[
            {
                "school": "Western Governors University",
                "degree": "M.Sc. in SWE",
                "years": "2025–2026",
            },
            {
                "school": "Florida State University",
                "degree": "B.Sc. in CS",
                "years": "2021–2024",
            },
        ],
    )


@app.route("/hobbies")
def hobbies():
    return render_template(
        "hobbies.html",
        title="Hobbies",
        hobbies=[
            {"name": "Running", "image": "running.png"},
            {"name": "Weightlifting", "image": "weightlifting.png"},
            {"name": "Reading", "image": "reading.png"},
        ],
    )


@app.route("/map")
def map():
    places = [
        {"name": "London", "lat": 51.5072, "lon": -0.1276, "date": "Dec 2019"},
        {"name": "Paris", "lat": 48.8566, "lon": 2.3522, "date": "Dec 2019"},
        {"name": "Madrid", "lat": 40.4168, "lon": -3.7038, "date": "Dec 2024"},
        {"name": "Toronto", "lat": 43.6511, "lon": -79.3837, "date": "Dec 2023"},
        {"name": "Dublin", "lat": 53.3498, "lon": -6.2603, "date": "Dec 2024"},
    ]
    return render_template("map.html", places=places)
