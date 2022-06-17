import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

'''
    dynamic navigation bar
    url: the url for the link, list
    people: all the people pages, list
    label: what to call the link, list
'''
class nav:
    def __init__(self, url, people, label):
        self.url = url
        self.people = people
        self.label = label

profile_nav = nav(
    ["", "work_edu", "hobbies"],
    ["william"],
    ["About Me", "Work Experience/Education", "Hobbies"]
)

@app.route('/')
def index():
    return render_template('index.html', nav=profile_nav, title="MLH Fellow", url=os.getenv("URL"))


# for william page
@app.route('/william')
def william():
    return render_template('william.html', nav=profile_nav, title="William", url=os.getenv("URL"))

# for work experience/education page
@app.route('/work_edu/<name>')
def work_edu(name):
    profile_title = name.capitalize()
    job = {
        "william": ["U.S. Census Bureau"]
    }
    # key: name
    # value: 2d list with inner generating new lines
    job_description = {
        "william": [["August 2020 - November 2020"]]
    }
    education = {
        "william": ["University of Chicago", "Stuyvesant High School"]
    }
    # key: name
    # value: 2d list with inner generating new lines
    edu_description = {
        "william": [["B.S. Computer Science, Minor in Philosophy", "Sept 2020 - June 2024"], ["High School", "Sept 2016 - June 2020"]]
    }
    profile_edu = education[name]
    profile_edu_desc = edu_description[name]
    profile_job = job[name]
    profile_job_desc = job_description[name]
    return render_template("work_edu.html", nav=profile_nav, job=profile_job, job_description=profile_job_desc, education=profile_edu, 
            edu_description=profile_edu_desc, title=profile_title, url=os.getenv("URL"))

# for work experience/education page
@app.route('/hobbies/<name>')
def hobbies(name):
    profile_title = name.capitalize()
    hobbies = {
        "william": ["dance, volleyball, gaming, tv series"]
    }
    profile_hobby = hobbies[name]
    photos = {
        "william": "william_hobby.jpg"
    }
    return render_template("hobbies.html", nav=profile_nav, hobbies=profile_hobby, title=profile_title, photo=photos[name], url=os.getenv("URL"))


# for map page
@app.route('/map')
def map():
    return render_template('map.html', nav=profile_nav, title="Map", url=os.getenv("URL"))