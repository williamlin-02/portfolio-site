import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
            user = os.getenv("MYSQL_USER"),
            password = os.getenv("MYSQL_PASSWORD"),
            host = os.getenv("MYSQL_HOST"),
            port = 3306)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

'''
    dynamic navigation bar
    url: the url for the link, list
    people: all the people pages, list
    label: what to call the link, list
'''

@app.route('/')
def index():
    return render_template('index.html', url=os.getenv("URL"))

# for william page
@app.route('/william')
def william():
    return render_template('william.html', title="William", url=os.getenv("URL"))

# for projects page
@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects", url=os.getenv("URL"))

# for map page
@app.route('/map')
def map():
    return render_template('map.html', title="Map", url=os.getenv("URL"))

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    get_name = request.form.get('name')
    get_email = request.form.get('email')
    get_content = request.form.get('content')

    if get_name is None or get_name == "":
        return "Invalid name", 400
    else:
        name = request.form['name']
    
    if "@" not in get_email or get_email is None:
        return "Invalid email", 400
    else:
        email = request.form['email']

    if get_content is None or get_content == "":
        return "Invalid content", 400
    else: 
        content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

# not working yet
# @app.route('/api/timeline_post', methods=['DELETE'])
# def delete_time_line_post():
#     model_to_dict(p)
#     for p in TimelinePost.select().delete_by_id(p.id)

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")

if __name__ == "__main__":
    app.run(debug=True)