from . import app1
from project import db

@app1.route('/')
def home():
    return 'hello world'