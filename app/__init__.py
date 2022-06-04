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