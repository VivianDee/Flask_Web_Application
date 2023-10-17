#!/usr/bin/python3
from flask import Flask


def create_app():
    """Initialize Flask"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'htjdjjnjfisikdlmkiwiuufredwckmdkjnujjr'
    
    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
