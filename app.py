from flask import Flask
from config import get_config
import os


app = Flask(__name__)

app.config.from_object(get_config())

# register blueprints
from views.root import *

if __name__ == '__main__':
    app.run()
   