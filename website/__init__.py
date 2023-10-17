#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    """Initialize Flask"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'htjdjjnjfisikdlmkiwiuufredwckmdkjnujjr'
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        print('Usage: ./main.py password')
        exit(1)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{sys.argv[1]}@localhost/bincomphptest'
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
