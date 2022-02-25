from flask import Flask
from config import config_options

app = Flask(__name__)

from app import views

app.config.from_object(config_options['devConfig'])

