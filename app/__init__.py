import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

# for amber page
@app.route('/amber')
def amber():
    return render_template('amber.html', title="Amber", url=os.getenv("URL"))

# for jacky page
@app.route('/jacky')
def jacky():
    return render_template('jacky.html', title="Jacky", url=os.getenv("URL"))

# for william page
@app.route('/william')
def william():
    return render_template('william.html', title="William", url=os.getenv("URL"))

# for work experience/education page
@app.route('/work_edu/<name>')
def work_edu(name):
    profile_title = name.capitalize()
    education = {
        "amber": ["edu"],
        "jacky": ["University of Kansas", "Northwest High School"],
        "william": ["edu"]
    }
    description = {
        "amber" : ["edu"],
        "jacky" : ["B.S. Computer Science\nAug 2020 - May 2024", "High School\nAug 2016 - May 2020"],
        "william" : ["edu"]
    }
    profile_edu = education[name]
    profile_desc = description[name]
    return render_template("work_edu.html", education=profile_edu, description=profile_desc, title=profile_title, url=os.getenv("URL"))

# for map page
@app.route('/map')
def map():
    return render_template('map.html', title="Map", url=os.getenv("URL"))