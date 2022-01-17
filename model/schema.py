from datetime import datetime
from enum import unique
from rest import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader 
def load_user(user_id):
    return Employee.query.get(int(user_id))

class Employee(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    employee_id = db.Column(db.String(10),unique=True)
    phone = db.Column(db.String(10))
    password = db.Column(db.String(30))
    role = db.Column(db.String(30))
    
class Workdetail(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    owner = db.Column(db.String(10),nullable=False)
    start = db.Column(db.DateTime)
    stop = db.Column(db.DateTime)
    minute = db.Column(db.Float)
    ot_minute = db.Column(db.String(50))
    amount = db.Column(db.Float)
    
    
    