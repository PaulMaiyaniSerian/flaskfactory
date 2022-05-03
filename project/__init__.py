from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    

    # attach routes and custom error pages here

    from app1.views import app1 as main_blueprint
    from app2.views import app2 as app2_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(app2_blueprint)


    return app