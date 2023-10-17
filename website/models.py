#!/usr/bin/python3
from . import db
from sqlalchemy.sql import func

class Announced_pu_results(db.Model):
    __tablename__ = 'announced_pu_results'

    result_id = db.Column(db.Integer, nullable=False, autoincrement=True)
    polling_unit_uniqueid = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False)
    user_ip_address = db.Column(db.String(50), nullable=False)


class Announced_ward_results(db.Model):
    __tablename__ = 'announced_ward_results'

    result_id = db.Column(db.Integer, nullable=False, autoincrement=True)   
    ward_name = db.Column(db.String(50), nullable=False)        
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)       
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False)
    user_ip_address = db.Column(db.String(50), nullable=False, primary_k)


class Announced_state_results(db.Model):
   __tablename__ = 'announced_state_results'

    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False)
    user_ip_address = db.Column(db.String(50), nullable=False)


class Announced_lga_results(db.Model):
    __tablename__ = 'announced_lga_results'

    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    lga_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False)
    user_ip_address = db.Column(db.String(50), nullable=False)
