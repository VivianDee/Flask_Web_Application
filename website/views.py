#!/usr/bin/python3
from flask import Blueprint, render_template
from .models import Announced_pu_results
from . import db




views = Blueprint('views', __name__)

@views.route('/')
def home():
    """homepage as root"""
    return render_template("home.html")

@views.route('/result')
def result():
    """Result page"""
    try:
        all_results = db.session.query(Announced_pu_results).all()
        print(all_results)
        return render_template("result.html")
    except Exception as e:
        print(f"Error: {e}")
        return "<p>An error occurred while fetching data.<p>"

@views.route('/sum')
def sum():
    """sum page"""
    return render_template("sum.html")

@views.route('/total')
def total():
    """total page"""
    return render_template("total.html")
