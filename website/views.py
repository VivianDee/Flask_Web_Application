#!/usr/bin/python3
from flask import Blueprint, render_template
from . import models

views = Blueprint('views', __name__)

@views.route('/')
def home():
    """homepage as root"""
    return render_template("home.html")

@views.route('/result')
def result():
    """Result page"""
    all_results = models.Announced_pu_results.query.all()
    return render_template("result.html", result=all_results)

@views.route('/sum')
def sum():
    """sum page"""
    return render_template("sum.html")

@views.route('/total')
def total():
    """total page"""
    return render_template("total.html")
