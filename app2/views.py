from flask import Blueprint
from project import db

app2 = Blueprint('app2', __name__)


@app2.route('/app2')
def another():
    return '<h1>hello world</h1>'