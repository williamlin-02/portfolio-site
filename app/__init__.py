import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, static_url_path = '/static')


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
    job = {
        "amber": ["Black Stallion Winery"],
        "jacky": ["Wendy's"],
        "william": ["job"]
    }
    # key: name
    # value: 2d list with inner generating new lines
    job_description = {
        "amber": [["July 2019 - June 2020"]],
        "jacky": [["October 2019 - March 2020"]],
        "william": [["job"]]
    }
    education = {
        "amber": ["University of Pennsylvania", "University of California, Davis"],
        "jacky": ["University of Kansas", "Northwest High School"],
        "william": ["edu"]
    }
    # key: name
    # value: 2d list with inner generating new lines
    edu_description = {
        "amber": [["M.S Computer and Information Technology","Aug 2021 - May 2023"], ["Viticulture and Enology","Sep 2015 - Jun 2018"]],
        "jacky": [["B.S. Computer Science","Aug 2020 - May 2024"], ["High School", "Aug 2016 - May 2020"]],
        "william": [["edu"]]
    }
    profile_edu = education[name]
    profile_edu_desc = edu_description[name]
    profile_job = job[name]
    profile_job_desc = job_description[name]
    return render_template("work_edu.html", job=profile_job, job_description=profile_job_desc, education=profile_edu, 
            edu_description=profile_edu_desc, title=profile_title, url=os.getenv("URL"))

# for work experience/education page
@app.route('/hobbies/<name>')
def hobbies(name):
    profile_title = name.capitalize()
    hobbies = {
        "amber": ["Travelling, Photography, Wine, Baking"],
        "jacky": ["hobbies"],
        "william": ["dance, volleyball, gaming, tv series"]
    }
    profile_hobby = hobbies[name]
    return render_template("hobbies.html", hobbies=profile_hobby, title=profile_title, url=os.getenv("URL"))


# for map page
@app.route('/map')
def map():
    return render_template('map.html', title="Map", url=os.getenv("URL"))