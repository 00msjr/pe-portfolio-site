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
                "position": "Developer",
                "company": "ABC Inc",
                "years": "2021–2023",
                "description": "Built web apps",
            },
            {
                "position": "Intern",
                "company": "XYZ Labs",
                "years": "2020",
                "description": "Helped with testing",
            },
        ],
        education=[{"school": "Uni A", "degree": "B.Sc. in CS", "years": "2017–2021"}],
    )


@app.route("/hobbies")
def hobbies():
    return render_template(
        "hobbies.html",
        title="Hobbies",
        hobbies=[
            {"name": "Hiking", "image": "hiking.jpg"},
            {"name": "Photography", "image": "photography.jpg"},
            {"name": "Cooking", "image": "cooking.jpg"},
        ],
    )



@app.route("/map")
def map():
    places = [
        {"name": "Tokyo", "lat": 35.6895, "lon": 139.6917, "date": "Jan 2023"},
        {"name": "Paris", "lat": 48.8566, "lon": 2.3522, "date": "May 2022"},
        {"name": "New York", "lat": 40.7128, "lon": -74.0060, "date": "Aug 2021"},
    ]
    return render_template("map.html", places=places)
