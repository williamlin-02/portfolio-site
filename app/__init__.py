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


if __name__ == "__main__":
    app.run(debug=True)