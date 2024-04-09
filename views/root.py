from flask import render_template
from app import app


@app.route('/')
def index():
    # get pyhton version
    import sys
    python_version = sys.version.split()[0]
    # get flask version
    import flask
    flask_version = flask.__version__ 
    return render_template('index.html', python_version=python_version, flask_version=flask_version)