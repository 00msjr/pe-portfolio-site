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
                "position": "Developer Intern",
                "company": "Direct Agents",
                "years": "February 2025-May 2025",
                "description": "Streamlined workflows",
            },
            {
                "position": "Data Analytics Intern",
                "company": "NYC Department of Investigation",
                "years": "February 2023-May 2023",
                "description": "Analyzed data",
            },
        ],
        education=[ {"school": "New York University", "degree": "MS in Computing", "years": "Expected Graduation December 2025"},{"school": "New York University", "degree": "BA in Computer Science", "years": "Graduated May 2024"}],
    )


@app.route("/hobbies")
def hobbies():
    return render_template(
        "hobbies.html",
        title="Hobbies",
        hobbies=[
            {"name": "Video Games", "image": "videogame.jpg"},
            {"name": "Reading", "image": "reading.jpg"}
        ],
    )



@app.route("/map")
def map():
    places = [
        {"name": "New York", "lat": 40.7128, "lon": -74.0060, "date": "Present"},
        {"name": "Toronto", "lat": 43.651070, "lon": -79.347015, "date": "June 2025"},
        {"name": "Amsterdam", "lat": 52.3676, "lon": 4.9041, "date": "May 2025"},
        {"name": "San Francisco", "lat": 37.7749, "lon": -122.4194, "date": "July 2024"},
        {"name": "Los Angeles", "lat": 34.0522, "lon": -118.2437, "date": "June 2024"},
        {"name": "Cancun", "lat": 21.1619, "lon": -86.8515, "date": "July 2015"},
        {"name": "Honolulu", "lat": 21.3069, "lon": -157.8583, "date": "June 2014"},
        {"name": "Paris", "lat": 48.8566, "lon": 2.3522, "date": "2011"},
        {"name": "London", "lat": 51.5074, "lon": -0.1278, "date": "2010"},
        {"name": "Beijing", "lat": 39.9042, "lon": 116.4074, "date": "2006"}

    ]
    return render_template("map.html", places=places)
