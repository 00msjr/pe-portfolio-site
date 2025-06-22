import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", title="Home")


@app.route("/profile")
def profile():
    return render_template(
        "profile.html",
        title="My Profile",
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


@app.route("/About")
def about():
    return render_template("about.html", title="About")
