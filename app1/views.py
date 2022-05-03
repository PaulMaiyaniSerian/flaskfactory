from flask import Blueprint
from project import db

app1 = Blueprint('app1', __name__)


@app1.route('/')
def home():
    return 'hello world'