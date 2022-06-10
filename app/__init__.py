from flask import Flask,redirect,render_template

app = Flask(__name__)

from app.models import *
from app.routes import *